<script>
    export let podcasts;
    export let techs;
    import Icon from '@iconify/svelte';

    import badrequestphoto from '$lib/assets/badrequest2.png';
    import visitarobotica from '$lib/assets/visita.png';

    const images = {
        'badrequest2.png': badrequestphoto,
        'visita.png': visitarobotica
    };
</script>

<section id="podcasts" class="mx-auto max-w-screen-lg px-3 py-12 md:py-16 animate-fade-in">
	<h2 class="mb-6 text-2xl font-bold">
		<div class="flex items-baseline justify-between">
			<div>
				Escucha mis <span class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent">podcasts</span>
			</div>
		</div>
	</h2>
	<div class="grid grid-cols-1 gap-6 md:grid-cols-2">
        {#each podcasts as pod }
            <div class="overflow-hidden rounded-md bg-slate-800 hover:-translate-y-1 transition-transform">
                <img
                    class="aspect-video w-full object-cover object-center"
                    src={images[pod.logo]}
                    loading="lazy"
                    alt={pod.title}
                />
                <div class="px-3 pt-4 pb-6 text-center">
                    <h3 class="text-xl font-semibold">{pod.title}</h3>
                    <div class="mt-2 text-sm">
                        {pod.description}
                    </div>
                </div>

                <div class="flex flex-col items-center gap-y-2 my-5">
                    <div class="grid grid-cols-3 items-center md:grid-cols-3 ">
                        {#each pod.platform as podi }
                            {#each techs as t}
                                {#if t.name === podi.title}
                                <a href={podi.url} target="_blank" rel="noopener" aria-label={`${pod.title} en ${podi.title}`}>
                                    <Icon icon={t.icon} class="h-10 w-10 transition-transform hover:-translate-y-1 m-3" loading="lazy"/>
                                </a>
                                {/if}        
                            {/each}
                        {/each}
                    </div>

                </div>

            </div>
            
        {/each}
	</div>
</section>