<script>
	export let socials;
	import Icon from '@iconify/svelte';

	const year = new Date().getFullYear();
</script>

<footer class="mx-auto max-w-screen-lg px-3 py-12 md:py-16 animate-fade-in">
	<div class="border-t border-gray-600 pt-5 md:flex md:items-center md:justify-between md:p-6">
		<div class="text-sm text-gray-200">
			© {year} Eduardo Saavedra · <a class="text-sky-400 hover:text-sky-300" href="mailto:eduar766@gmail.com">eduar766@gmail.com</a>
			<div class="mt-1 text-gray-400">
				Hecho con <span class="font-bold"><a class="hover:text-white" href="https://kit.svelte.dev/" target="_blank" rel="noopener">SvelteKit</a> + <a class="hover:text-white" href="https://tailwindcss.com/" target="_blank" rel="noopener">TailwindCSS</a></span>
			</div>
		</div>

		<div class="flex flex-wrap items-center mt-3 text-sm sm:mt-0">
			<a href="https://github.com/eduar766/my_cv" target="_blank" rel="noopener" class="flex items-center justify-center rounded-md bg-white px-4 py-1 text-sm font-medium text-slate-900 shadow-sm transition-opacity hover:opacity-90">
				{#each socials as s}
					{#if s.id === 2}
						<Icon icon={s.icon} class="h-8 w-8" loading="lazy"/>
					{/if}
				{/each}

				<span class="ml-2">Ver el código</span>
			</a>
		</div>
	</div>
</footer>
