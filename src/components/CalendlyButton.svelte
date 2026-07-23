<script>
    import Icon from '@iconify/svelte';

    export let url = 'https://calendly.com/eduardo-saavedra';
    export let label = 'Agendar una llamada';
    export let variant = 'primary';
    export let compact = false;
    let className = '';
    export { className as class };

    $: sizeClasses = compact ? 'px-4 py-2 text-sm' : 'px-6 py-3';

    let open = false;

    function openModal() {
        open = true;
        document.body.style.overflow = 'hidden';
    }

    function closeModal() {
        open = false;
        document.body.style.overflow = '';
    }

    function handleKeydown(event) {
        if (event.key === 'Escape') closeModal();
    }

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
        class="inline-block rounded-md bg-gradient-to-br from-sky-500 to-cyan-400 {sizeClasses} font-semibold text-white transition-all hover:-translate-y-0.5 hover:shadow-lg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-sky-400 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-900 {className}"
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
        aria-label="Calendly scheduling"
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
            <button
                on:click={closeModal}
                class="absolute right-3 top-3 z-10 rounded-full bg-slate-700 p-2 text-white transition-colors hover:bg-slate-600"
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
            ></iframe>
        </div>
    </div>
{/if}
