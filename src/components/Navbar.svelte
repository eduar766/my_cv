<script>
    export let socials;
</script>

<div class="mx-auto max-w-screen-lg px-3 py-6">
	<div class="flex flex-col gap-y-3 sm:flex-row sm:items-center sm:justify-between">
		<a href="/">
            <div class="flex items-center bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-xl font-bold text-transparent">
				Eduardo Saavedra
			</div>
        </a>
		<nav>
			<ul class="flex gap-x-3 font-medium text-gray-200">
                {#each socials as social }
                    {#if social.id === 5}
                        <li class="hover:text-white">
                            <a href={`${social.url}`}>Blogs</a>
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
</div>
