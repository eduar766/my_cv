<script>
    import Icon from '@iconify/svelte';

    export let about;
    export let socials;
    export let profession;
	import photo from '$lib/assets/avatar.svg';
</script>

<div class="mx-auto max-w-screen-lg px-3 py-6 animate-fade-in">
	<div class="flex flex-col items-center md:flex-row md:justify-between md:gap-x-24">
		<div>
			<h1 class="text-3xl font-bold">
				Hi there, I'm 
                <span class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent">Eduardo</span
				> 👋
			</h1>
			<p class="mt-2 text-lg text-gray-300">{profession}</p>
			<p class="mt-6 text-xl leading-9">
                {about}
                

			</p>
			<div class="mt-3 flex gap-1">
                {#each socials as social }
                    <a href={`${social.url}`}>
                        <Icon icon={social.icon} class="h-12 w-12 hover:translate-y-1" loading="lazy"/>
                    </a>
                {/each}
			</div>
            <div class="mt-6">
                <a href="https://www.linkedin.com/in/eduardo-saavedra/" class="inline-block rounded-md bg-gradient-to-br from-sky-500 to-cyan-400 px-6 py-3 font-semibold text-white transition-all hover:translate-y-0.5 hover:shadow-lg">
                    Contact me
                </a>
            </div>
		</div>
		<div class="shrink-0">
			<img class="h-80 w-64" src={photo} alt="Edu" loading="lazy" />
		</div>
	</div>
</div>
