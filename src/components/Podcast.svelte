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

<section id="podcasts" class="page-section">
	<div class="section-heading">
		<div>
			<p class="eyebrow">Fuera del editor de código</p>
			<h2>También detrás del micrófono<span class="text-sky-400">.</span></h2>
		</div>
		<p>Conversaciones sobre programación, tecnología y todo lo que despierta mi curiosidad.</p>
	</div>
	<div class="grid grid-cols-1 gap-6 md:grid-cols-2">
		{#each podcasts as pod}
			<div class="podcast-card">
				<img
					class="aspect-video w-full object-cover object-center"
					src={images[pod.logo]}
					loading="lazy"
					alt={pod.title}
				/>
				<div class="px-6 pt-5 pb-2">
					<h3 class="text-xl font-semibold">{pod.title}</h3>
					<div class="mt-2 text-sm">
						{pod.description}
					</div>
				</div>

				<div class="flex flex-col items-start px-3 pb-4">
					<div class="grid grid-cols-3 items-center md:grid-cols-3">
						{#each pod.platform as podi}
							{#each techs as t}
								{#if t.name === podi.title}
									<a
										href={podi.url}
										target="_blank"
										rel="noopener"
										aria-label={`${pod.title} en ${podi.title}`}
									>
										<Icon
											icon={t.icon}
											class="h-10 w-10 transition-transform hover:-translate-y-1 m-3"
											loading="lazy"
										/>
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
