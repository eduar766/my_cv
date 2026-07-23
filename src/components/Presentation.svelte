<script>
    import Icon from '@iconify/svelte';
    import CalendlyButton from './CalendlyButton.svelte';

    export let about;
    export let socials;
    export let headline;
	import photo from '$lib/assets/avatar.svg';
</script>

<section id="about" class="mx-auto max-w-screen-lg px-3 py-12 md:py-16 animate-fade-in">
	<div class="flex flex-col items-center md:flex-row md:justify-between md:gap-x-24">
		<div>
			<p class="text-lg font-medium text-gray-400">Hola, soy 👋</p>
			<h1 class="mt-1 text-4xl font-bold md:text-5xl">
                Eduardo <span class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent">Saavedra</span><span class="sr-only"> — Consultor AWS y Technical Lead en Santiago de Chile</span>
			</h1>
			<p class="mt-2 text-lg font-semibold text-sky-400">
                Technical Lead &amp; Consultor AWS
            </p>
			<p class="mt-4 text-xl font-medium text-gray-100">
                {headline}
            </p>
			<p class="mt-4 text-lg leading-8 text-gray-300">
                {about}
			</p>
			<div class="mt-3 flex gap-1">
                {#each socials as social }
                    <a href={`${social.url}`} aria-label={social.title} target="_blank" rel="noopener">
                        <Icon icon={social.icon} class="h-12 w-12 transition-transform hover:-translate-y-1" loading="lazy"/>
                    </a>
                {/each}
			</div>
            <div class="mt-6 flex flex-col gap-3 sm:flex-row">
                <CalendlyButton label="Agendar una llamada" variant="primary" />
                <a href="#experience" class="inline-block rounded-md border border-sky-500 px-6 py-3 font-semibold text-sky-400 transition-all hover:bg-sky-500/10 hover:-translate-y-0.5 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-sky-400 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-900">
                    Ver mi experiencia
                </a>
            </div>
		</div>
		<div class="shrink-0">
			<img class="h-80 w-64" src={photo} alt="Eduardo Saavedra avatar" loading="lazy" />
		</div>
	</div>
</section>
