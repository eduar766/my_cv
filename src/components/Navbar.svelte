<script>
    export let socials;
    let scrolled = false;

    function handleScroll() {
        scrolled = window.scrollY > 60;
    }
</script>

<svelte:window on:scroll={handleScroll}/>

<header class="sticky top-0 z-50 mx-auto w-full bg-slate-900/80 backdrop-blur-md px-3 py-6 transition-all {scrolled ? 'shadow-lg shadow-black/20' : ''}">
	<div class="mx-auto flex max-w-screen-lg flex-col gap-y-3 sm:flex-row sm:items-center sm:justify-between">
		<a href="/" aria-label="Home">
            <div class="flex items-center bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-xl font-bold text-transparent">
				Eduardo Saavedra
			</div>
        </a>
		<nav>
			<ul class="flex gap-x-3 font-medium text-gray-200">
                {#each socials as social }
                    {#if social.id === 5}
                        <li class="hover:text-white">
                            <a href={`${social.url}`}>Instagram</a>
                        </li>
                    {:else if social.id === 2}
                        <li class="hover:text-white">
                            <a href={`${social.url}`}>GitHub</a>
                        </li>
                    {:else if social.id === 3}
                        <li class="hover:text-white">
                            <a href={`${social.url}`}>Twitter</a>
                        </li>
                    {/if}
                {/each}
			</ul>
		</nav>
	</div>
</header>
