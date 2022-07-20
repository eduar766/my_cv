<script>
	export let socials;
	import Icon from '@iconify/svelte';
</script>

<div class="mx-auto max-w-screen-lg px-3 py-6">
	<div class="border-t border-gray-600 pt-5 md:flex md:items-center md:justify-between md:p-6">
		<div class="text-sm text-gray-200">© Copyright 2022. Built with  <sapan class="font-bold"><a href="https://kit.svelte.dev/">SvelteKit</a> + <a href="https://tailwindcss.com/">TailwindCSS</a></sapan></div>

		<div class="flex flex-wrap items-center mt-3 text-sm text-gray-500 dark:text-gray-400 sm:mt-0">
			<a href="https://github.com/eduar766/my_cv" class="flex items-center justify-center px-4 border border-transparent rounded-md shadow-sm text-sm font-medium dark:text-primary dark:bg-white hover:dark:bg-opacity-90 hover:cursor-pointer py-1 text-slate-900">
				{#each socials as s}
					{#if s.id === 2}
						<Icon icon={s.icon} class="h-8 w-8" loading="lazy"/>
					{/if}
				{/each}
				
				<span class="ml-2">Check this project</span>
			</a>
		</div>
	</div>
	
</div>
