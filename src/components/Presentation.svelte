<script>
    import Icon from '@iconify/svelte';
    import CalendlyButton from './CalendlyButton.svelte';

    export let about;
    export let socials;
    export let headline;
	import photo from '$lib/assets/avatar.svg';
</script>

<section id="about" class="mx-auto max-w-screen-lg px-3 py-6 animate-fade-in">
	<div class="flex flex-col items-center md:flex-row md:justify-between md:gap-x-24">
		<div>
			<h1 class="text-3xl font-bold">
				Hi there, I'm 
                <span class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent">Eduardo</span
				> 👋
			</h1>
			<p class="mt-2 text-xl font-semibold text-sky-400">
                {headline}
            </p>
			<p class="mt-6 text-lg leading-8 text-gray-300">
                {about}
			</p>
			<div class="mt-3 flex gap-1">
                {#each socials as social }
                    <a href={`${social.url}`} aria-label={social.title}>
                        <Icon icon={social.icon} class="h-12 w-12 hover:translate-y-1" loading="lazy"/>
                    </a>
                {/each}
			</div>
            <div class="mt-6 flex flex-col gap-3 sm:flex-row">
                <CalendlyButton label="Agenda una llamada" variant="primary" />
                <a href="#services" class="inline-block rounded-md border border-sky-500 px-6 py-3 font-semibold text-sky-400 transition-all hover:bg-sky-500/10 hover:translate-y-0.5">
                    Ver servicios
                </a>
            </div>
		</div>
		<div class="shrink-0">
			<img class="h-80 w-64" src={photo} alt="Eduardo Saavedra avatar" loading="lazy" />
		</div>
	</div>
</section>
