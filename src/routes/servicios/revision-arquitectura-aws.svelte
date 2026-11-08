<script context="module">
	export const prerender = true;
</script>

<script>
	import Navbar from '../../components/Navbar.svelte';
	import Footer from '../../components/Footer.svelte';
	import CalendlyButton from '../../components/CalendlyButton.svelte';
	import data from '../../eduardo.json';

	const SITE = 'https://www.saavedratech.dev';
	const PAGE = `${SITE}/servicios/revision-arquitectura-aws`;

	const faqs = [
		{
			question: '¿Cuánto dura una revisión de arquitectura AWS?',
			answer:
				'Entre 1 y 3 semanas según el tamaño de la cuenta y la cantidad de workloads. El resultado se entrega en una sesión de 60 minutos junto con el informe escrito.'
		},
		{
			question: '¿Necesito dar acceso a mi cuenta de AWS?',
			answer:
				'Sí, con un rol de solo lectura (ReadOnlyAccess o SecurityAudit). Nunca pido credenciales de administrador ni realizo cambios directos sobre la infraestructura.'
		},
		{
			question: '¿La revisión sigue el Well-Architected Framework?',
			answer:
				'Uso el Well-Architected Framework de AWS como base (excelencia operativa, seguridad, fiabilidad, eficiencia de rendimiento, optimización de costos y sostenibilidad), pero el foco está en lo que realmente corre en producción, no en un checklist genérico.'
		},
		{
			question: '¿Qué pasa después de la revisión?',
			answer:
				'Recibes un plan de acción por fases con impacto estimado. Puedes implementarlo con tu equipo, o puedo acompañar la implementación como Technical Lead fractional.'
		}
	];

	const structuredData = {
		'@context': 'https://schema.org',
		'@graph': [
			{
				'@type': 'Service',
				'@id': `${PAGE}#service`,
				name: 'Revisión de arquitectura AWS',
				serviceType: 'Auditoría de arquitectura cloud',
				url: PAGE,
				description:
					'Auditoría práctica de cuentas AWS en producción: estabilidad, costos, seguridad y escalabilidad, basada en el Well-Architected Framework. Entrega informe priorizado, diagrama de arquitectura y plan de acción por fases.',
				provider: {
					'@type': 'Person',
					'@id': `${SITE}/#eduardo`,
					name: 'Eduardo Saavedra',
					jobTitle: 'Consultor AWS & Technical Lead',
					url: SITE + '/',
					sameAs: data.socials.map((s) => s.url)
				},
				areaServed: [
					{ '@type': 'Country', name: 'Chile' },
					{ '@type': 'AdministrativeArea', name: 'Latinoamérica' }
				],
				availableLanguage: ['es', 'en']
			},
			{
				'@type': 'FAQPage',
				'@id': `${PAGE}#faq`,
				mainEntity: faqs.map((f) => ({
					'@type': 'Question',
					name: f.question,
					acceptedAnswer: { '@type': 'Answer', text: f.answer }
				}))
			},
			{
				'@type': 'BreadcrumbList',
				itemListElement: [
					{ '@type': 'ListItem', position: 1, name: 'Inicio', item: SITE + '/' },
					{ '@type': 'ListItem', position: 2, name: 'Revisión de arquitectura AWS', item: PAGE }
				]
			}
		]
	};

	const jsonLd = `<script type="application/ld+json">${JSON.stringify(
		structuredData
	)}${'<'}/script>`;
</script>

<svelte:head>
	<title>Revisión de arquitectura AWS en Chile y LATAM | Eduardo Saavedra</title>
	<meta
		name="description"
		content="Auditoría práctica de tu cuenta AWS: estabilidad, costos, seguridad y escalabilidad según el Well-Architected Framework. Informe priorizado, diagrama y plan de acción por fases."
	/>
	<link rel="canonical" href="https://www.saavedratech.dev/servicios/revision-arquitectura-aws" />
	{@html jsonLd}
</svelte:head>

<Navbar />

<main id="main-content" class="service-page">
	<nav class="mb-6 text-sm text-gray-400" aria-label="Breadcrumb">
		<a href="/" class="hover:text-white">Inicio</a> <span aria-hidden="true">/</span> Revisión de arquitectura
		AWS
	</nav>

	<h1 class="text-3xl font-bold md:text-4xl">
		Revisión de <span
			class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent"
			>arquitectura AWS</span
		>
	</h1>

	<p class="mt-6 text-lg leading-8 text-gray-300">
		Una revisión de arquitectura AWS es una auditoría técnica de tu cuenta en producción que evalúa
		cuatro dimensiones: <strong class="text-gray-100"
			>estabilidad, costos, seguridad y escalabilidad</strong
		>. La hago sobre lo que realmente corre en tu infraestructura — no sobre un checklist genérico —
		usando el Well-Architected Framework de AWS como base metodológica.
	</p>

	<h2 class="mt-10 text-2xl font-bold">Para quién es</h2>
	<ul class="mt-4 list-disc space-y-2 pl-5 text-gray-300">
		<li>Empresas cuya factura de AWS crece más rápido que su negocio.</li>
		<li>Equipos que sufren caídas o degradación bajo carga y no saben exactamente por qué.</li>
		<li>Startups que necesitan validar su arquitectura antes de escalar o levantar capital.</li>
		<li>CTOs que heredaron una cuenta AWS sin documentación y necesitan un mapa real.</li>
	</ul>

	<h2 class="mt-10 text-2xl font-bold">Cómo funciona</h2>
	<ol class="mt-4 list-decimal space-y-3 pl-5 text-gray-300">
		<li>
			<strong class="text-gray-100">Llamada de diagnóstico (30 min, sin costo):</strong> entendemos tu
			contexto, dolores y objetivos.
		</li>
		<li>
			<strong class="text-gray-100">Acceso de solo lectura:</strong> configuras un rol ReadOnly/SecurityAudit;
			nunca pido credenciales de administrador.
		</li>
		<li>
			<strong class="text-gray-100">Análisis (1-3 semanas):</strong> arquitectura y dependencias críticas,
			costos y oportunidades inmediatas, seguridad y networking, cuellos de botella de escalabilidad.
		</li>
		<li>
			<strong class="text-gray-100">Entrega:</strong> sesión de 60 minutos para revisar resultados con
			tu equipo.
		</li>
	</ol>

	<h2 class="mt-10 text-2xl font-bold">Qué recibes</h2>
	<ul class="mt-4 list-disc space-y-2 pl-5 text-gray-300">
		<li>Informe priorizado de hallazgos y riesgos, con impacto estimado.</li>
		<li>Diagrama actualizado de tu arquitectura.</li>
		<li>Plan de acción por fases, ordenado por retorno.</li>
		<li>Sesión de 60 minutos para revisar resultados.</li>
	</ul>

	<h2 class="mt-10 text-2xl font-bold">Experiencia que respalda este servicio</h2>
	<p class="mt-4 text-gray-300">
		Más de 10 años construyendo y operando plataformas sobre AWS en retail y fintech: en Cencosud
		lideré Moncap (gestión de capacidades a nivel nacional) y Balancer (optimización de ventanas
		horarias escalada a 5 países); hoy soy Technical Lead en BK Servicios Financieros.
	</p>

	<h2 class="mt-10 text-2xl font-bold">Preguntas frecuentes</h2>
	<div class="mt-4 space-y-3">
		{#each faqs as faq}
			<details class="group rounded-md bg-slate-800 p-4">
				<summary
					class="flex cursor-pointer list-none items-center justify-between gap-3 font-semibold text-gray-100 marker:content-none"
				>
					{faq.question}
					<span
						class="shrink-0 text-xl leading-none text-sky-400 transition-transform group-open:rotate-45"
						aria-hidden="true">+</span
					>
				</summary>
				<p class="mt-3 text-gray-300">{faq.answer}</p>
			</details>
		{/each}
	</div>

	<div class="mt-12 rounded-lg bg-slate-800 px-6 py-8 text-center">
		<h2 class="text-xl font-bold">¿Quieres saber cómo está tu cuenta AWS?</h2>
		<p class="mx-auto mt-2 max-w-md text-gray-300">
			Empecemos con una llamada de diagnóstico de 30 minutos, sin costo y sin compromiso.
		</p>
		<div class="mt-5 flex justify-center">
			<CalendlyButton label="Agendar diagnóstico gratuito" variant="primary" />
		</div>
	</div>
</main>

<Footer socials={data.socials} />
