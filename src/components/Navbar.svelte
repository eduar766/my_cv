<script>
    import CalendlyButton from './CalendlyButton.svelte';

    export let socials;
    let scrolled = false;

    function handleScroll() {
        scrolled = window.scrollY > 60;
    }
</script>

<svelte:window on:scroll={handleScroll}/>

<header class="sticky top-0 z-50 mx-auto w-full bg-slate-900/80 backdrop-blur-md px-3 py-3 md:py-4 transition-all {scrolled ? 'shadow-lg shadow-black/20' : ''}">
	<div class="mx-auto flex max-w-screen-lg flex-col gap-y-3 sm:flex-row sm:items-center sm:justify-between">
		<a href="/" aria-label="Home">
            <div class="flex items-center bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-xl font-bold text-transparent">
				Eduardo Saavedra
			</div>
        </a>
		<div class="flex flex-wrap items-center gap-x-4 gap-y-2">
			<nav>
				<ul class="flex flex-wrap items-center gap-x-3 gap-y-1 font-medium text-gray-200">
	                <li class="hover:text-white">
	                    <a href="#services">Servicios</a>
	                </li>
	                <li class="hover:text-white">
	                    <a href="#experience">Experiencia</a>
	                </li>
	                <li class="hover:text-white">
	                    <a href="#podcasts">Podcast</a>
	                </li>
	                {#each socials as social }
	                    {#if social.id === 2}
	                        <li class="hover:text-white">
	                            <a href={`${social.url}`} target="_blank" rel="noopener">GitHub</a>
	                        </li>
	                    {:else if social.id === 3}
	                        <li class="hover:text-white">
	                            <a href={`${social.url}`} target="_blank" rel="noopener">Medium</a>
	                        </li>
	                    {/if}
	                {/each}
				</ul>
			</nav>
			<CalendlyButton label="Agendar llamada" variant="primary" compact />
		</div>
	</div>
</header>
