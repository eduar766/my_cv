<script>
	import Icon from '@iconify/svelte';
	import { tick, onDestroy } from 'svelte';

	export let url = 'https://calendly.com/eduardo-saavedra';
	export let label = 'Agendar una llamada';
	export let variant = 'primary';
	export let compact = false;
	let className = '';
	export { className as class };

	$: sizeClasses = compact ? 'px-4 py-2 text-sm' : 'px-6 py-3';

	let open = false;

	let closeButton;
	let trigger;
	let previousOverflow = '';

	async function openModal() {
		open = true;
		trigger = document.activeElement;
		previousOverflow = document.body.style.overflow;
		document.body.style.overflow = 'hidden';
		await tick();
		closeButton?.focus();
	}

	function closeModal() {
		if (!open) return;
		open = false;
		document.body.style.overflow = previousOverflow;
		trigger?.focus();
	}

	function handleKeydown(event) {
		if (open && event.key === 'Escape') closeModal();
	}

	onDestroy(() => {
		if (open) document.body.style.overflow = previousOverflow;
	});

	function portal(node) {
		document.body.appendChild(node);
		return {
			destroy() {
				node.remove();
			}
		};
	}
</script>

<svelte:window on:keydown={handleKeydown} />

{#if variant === 'primary'}
	<button
		on:click={openModal}
		class="inline-block rounded-md bg-sky-300 {sizeClasses} font-semibold text-slate-950 transition-all hover:-translate-y-0.5 hover:shadow-lg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-sky-400 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-900 {className}"
	>
		{label}
	</button>
{:else}
	<button
		on:click={openModal}
		class="inline-block rounded-md border border-sky-500 {sizeClasses} font-semibold text-sky-400 transition-all hover:bg-sky-500/10 hover:-translate-y-0.5 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-sky-400 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-900 {className}"
	>
		{label}
	</button>
{/if}

{#if open}
	<div
		use:portal
		class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 p-4 backdrop-blur-sm"
		on:click={closeModal}
		role="dialog"
		aria-modal="true"
		aria-label="Agendar una conversación"
		tabindex="-1"
		on:keydown={handleKeydown}
	>
		<div
			class="relative w-full max-w-4xl overflow-hidden rounded-lg bg-slate-900 p-2 shadow-2xl"
			on:click|stopPropagation
			role="presentation"
			tabindex="-1"
			on:keydown={handleKeydown}
		>
			<span
				tabindex="0"
				role="button"
				aria-label="Ir al cierre del diálogo"
				on:focus={() => closeButton?.focus()}
			/>
			<button
				on:click={closeModal}
				class="absolute right-3 top-3 z-10 rounded-full bg-slate-700 p-2 text-white transition-colors hover:bg-slate-600"
				bind:this={closeButton}
				aria-label="Cerrar"
			>
				<Icon icon="mdi:close" class="h-5 w-5" />
			</button>
			<iframe
				src={url}
				title="Calendly"
				class="w-full rounded-md"
				style="height: 80vh; border: none;"
				loading="lazy"
			/>
			<span
				tabindex="0"
				role="button"
				aria-label="Volver al cierre del diálogo"
				on:focus={() => closeButton?.focus()}
			/>
		</div>
	</div>
{/if}
