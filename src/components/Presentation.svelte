<script>
	import Icon from '@iconify/svelte';
	import photo from '$lib/assets/eduardo-portrait.webp';
	export let socials;
</script>

<section id="about" class="page-section hero">
	<div class="hero-copy">
		<p class="eyebrow">Ingeniería · Productos · Personas</p>
		<h1>Hola, soy<br />Eduardo <span class="text-sky-400">Saavedra.</span></h1>
		<p class="hero-role">Technical Lead, ingeniero y creador de productos.</p>
		<p class="hero-description">
			Construyo software, diseño sistemas en AWS y acompaño a equipos a convertir ideas en
			productos. Más de 10 años entre tecnología, retail y servicios financieros.
		</p>
		<div class="hero-actions">
			<a class="button-primary" href="#projects"
				>Explorar mis proyectos <span aria-hidden="true">↗</span></a
			>
			<a
				class="text-link"
				href="/cv/eduardo-saavedra-cv-2026.pdf"
				download="Eduardo-Saavedra-CV-2026.pdf"
				>Descargar CV <span class="text-xs font-normal text-slate-400">PDF</span><span
					aria-hidden="true">↓</span
				></a
			>
		</div>
		<div class="hero-socials">
			<span>Santiago, Chile · Trabajo remoto</span>
			<div class="flex gap-4">
				{#each socials.slice(0, 3) as social}
					<a href={social.url} aria-label={social.title} target="_blank" rel="noopener noreferrer"
						><Icon icon={social.icon} class="h-5 w-5" /></a
					>
				{/each}
			</div>
		</div>
	</div>
	<figure class="hero-portrait">
		<img
			src={photo}
			alt="Retrato ilustrado de Eduardo Saavedra con gafas y jersey oscuro"
			width="1254"
			height="1254"
			fetchpriority="high"
		/>
	</figure>
</section>
<div class="credibility-strip">
	<div><strong>10+ años</strong><span>construyendo software</span></div>
	<div><strong>3 productos propios</strong><span>de la idea al desarrollo</span></div>
	<div><strong>Retail & fintech</strong><span>experiencia en sistemas reales</span></div>
</div>
