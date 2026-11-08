<script context="module">
	export const prerender = true;
</script>

<script>
	import Navbar from '../components/Navbar.svelte';
	import Presentation from '../components/Presentation.svelte';
	import Projects from '../components/Projects.svelte';
	import Services from '../components/Services.svelte';
	import Jobs from '../components/Jobs.svelte';
	import Skills from '../components/Skills.svelte';
	import Footer from '../components/Footer.svelte';
	import Podcast from '../components/Podcast.svelte';
	import ContactCta from '../components/ContactCta.svelte';
	import Faq from '../components/Faq.svelte';

	import data from '../eduardo.json';

	const SITE = 'https://www.saavedratech.dev';

	const structuredData = {
		'@context': 'https://schema.org',
		'@graph': [
			{
				'@type': 'Person',
				'@id': `${SITE}/#eduardo`,
				name: 'Eduardo Saavedra',
				givenName: 'Eduardo',
				familyName: 'Saavedra',
				jobTitle: 'Consultor AWS & Technical Lead',
				description: data.about,
				url: SITE + '/',
				sameAs: data.socials.map((s) => s.url),
				address: {
					'@type': 'PostalAddress',
					addressLocality: 'Santiago',
					addressCountry: 'CL'
				},
				knowsLanguage: ['es', 'en'],
				knowsAbout: [
					'Amazon Web Services (AWS)',
					'AWS Well-Architected Framework',
					'Optimización de costos AWS',
					'Arquitectura serverless (Lambda, SQS, SNS)',
					'Kubernetes (EKS)',
					'Terraform e Infraestructura como Código',
					'Agentes de IA y desarrollo asistido por IA',
					'Integraciones Salesforce',
					'NestJS y TypeScript',
					'PostgreSQL',
					'Liderazgo técnico y gestión de equipos'
				],
				hasOccupation: {
					'@type': 'Occupation',
					name: 'Consultor de arquitectura cloud AWS',
					occupationLocation: { '@type': 'Country', name: 'Chile' },
					skills: 'AWS, Kubernetes, Terraform, Serverless, FinOps, IA'
				},
				worksFor: { '@type': 'Organization', name: 'BK Servicios Financieros' },
				alumniOf: {
					'@type': 'CollegeOrUniversity',
					name: 'UNEFA',
					address: {
						'@type': 'PostalAddress',
						addressLocality: 'Anzoátegui',
						addressCountry: 'Venezuela'
					}
				}
			},
			{
				'@type': 'ProfessionalService',
				'@id': `${SITE}/#service-business`,
				name: 'SaavedraTech — Consultoría AWS',
				alternateName: 'SaavedraTech Digital Engineering',
				logo: `${SITE}/logo-full.png`,
				image: `${SITE}/og-image.png`,
				url: SITE + '/',
				founder: { '@id': `${SITE}/#eduardo` },
				description:
					'Consultoría de arquitectura AWS, optimización de costos cloud, aceleración con IA y liderazgo técnico fractional para empresas de Chile y Latinoamérica.',
				areaServed: [
					{ '@type': 'Country', name: 'Chile' },
					{ '@type': 'AdministrativeArea', name: 'Latinoamérica' }
				],
				availableLanguage: ['es', 'en'],
				priceRange: '$$',
				address: {
					'@type': 'PostalAddress',
					addressLocality: 'Santiago',
					addressCountry: 'CL'
				},
				hasOfferCatalog: {
					'@type': 'OfferCatalog',
					name: 'Servicios de consultoría',
					itemListElement: [
						{
							'@type': 'Offer',
							itemOffered: {
								'@type': 'Service',
								name: 'Revisión de arquitectura AWS',
								serviceType: 'Auditoría de arquitectura cloud',
								url: `${SITE}/servicios/revision-arquitectura-aws`,
								description:
									'Auditoría práctica de tu cuenta AWS enfocada en estabilidad, costo y seguridad, basada en el Well-Architected Framework. Incluye informe priorizado de hallazgos, diagrama de arquitectura y plan de acción por fases.',
								provider: { '@id': `${SITE}/#eduardo` },
								areaServed: { '@type': 'Country', name: 'Chile' }
							}
						},
						{
							'@type': 'Offer',
							itemOffered: {
								'@type': 'Service',
								name: 'Optimización de costos AWS',
								serviceType: 'FinOps / Optimización de costos cloud',
								url: `${SITE}/servicios/reducir-costos-aws`,
								description:
									'Reducción de la factura de AWS mediante right-sizing, Savings Plans, revisión de NAT Gateways, almacenamiento y eliminación de recursos huérfanos. Ahorros habituales del 20% al 40% en cuentas sin optimizar.',
								provider: { '@id': `${SITE}/#eduardo` }
							}
						},
						{
							'@type': 'Offer',
							itemOffered: {
								'@type': 'Service',
								name: 'Aceleración con IA',
								serviceType: 'Consultoría de Inteligencia Artificial',
								description:
									'Prototipos funcionales con agentes de IA en semanas: automatización de flujos internos y reducción del Time to Market de al menos 40%.',
								provider: { '@id': `${SITE}/#eduardo` }
							}
						},
						{
							'@type': 'Offer',
							itemOffered: {
								'@type': 'Service',
								name: 'Liderazgo técnico fractional',
								serviceType: 'Fractional Technical Lead / CTO',
								url: `${SITE}/servicios/liderazgo-tecnico-fractional`,
								description:
									'Dirección técnica a demanda: diseño de arquitectura, mentoría de equipos y definición de procesos, sin contratación a tiempo completo.',
								provider: { '@id': `${SITE}/#eduardo` }
							}
						}
					]
				}
			},
			{
				'@type': 'WebSite',
				'@id': `${SITE}/#website`,
				url: SITE + '/',
				name: 'Eduardo Saavedra — Ingeniero y creador de productos',
				inLanguage: 'es-CL',
				publisher: { '@id': `${SITE}/#eduardo` }
			},
			{
				'@type': 'FAQPage',
				'@id': `${SITE}/#faq`,
				mainEntity: [
					{
						'@type': 'Question',
						name: '¿Qué incluye una revisión de arquitectura AWS?',
						acceptedAnswer: {
							'@type': 'Answer',
							text: 'Incluye el análisis de la arquitectura actual y sus dependencias críticas, revisión de costos con oportunidades de optimización inmediata, evaluación de seguridad y networking, y detección de cuellos de botella de escalabilidad. Entrego un informe priorizado, un diagrama actualizado de la arquitectura y un plan de acción por fases, más una sesión de 60 minutos para revisar resultados.'
						}
					},
					{
						'@type': 'Question',
						name: '¿Trabajas con empresas fuera de Chile?',
						acceptedAnswer: {
							'@type': 'Answer',
							text: 'Sí. Estoy en Santiago de Chile y trabajo de forma remota con empresas de toda Latinoamérica, en español e inglés.'
						}
					},
					{
						'@type': 'Question',
						name: '¿Cuánto se puede reducir la factura de AWS?',
						acceptedAnswer: {
							'@type': 'Answer',
							text: 'Depende del estado de la cuenta, pero en cuentas sin optimizar es habitual encontrar ahorros del 20% al 40% mediante right-sizing, Savings Plans, revisión de NAT Gateways y almacenamiento, y eliminación de recursos huérfanos. La revisión identifica los ahorros de mayor impacto primero.'
						}
					},
					{
						'@type': 'Question',
						name: '¿Qué es un Technical Lead fractional?',
						acceptedAnswer: {
							'@type': 'Answer',
							text: 'Es un líder técnico senior que trabaja con tu equipo algunas horas o días por semana: define arquitectura, revisa decisiones técnicas, mentorea a los desarrolladores y prioriza deuda técnica, sin el costo de una contratación a tiempo completo.'
						}
					}
				]
			}
		]
	};

	const jsonLd = `<script type="application/ld+json">${JSON.stringify(
		structuredData
	)}${'<'}/script>`;
</script>

<svelte:head>
	<title>Eduardo Saavedra — Ingeniero, Technical Lead y creador de productos</title>
	<meta
		name="description"
		content="Conoce a Eduardo Saavedra: ingeniero, Technical Lead y creador de Futbocracy, Lazy CRM y Komorebi. Proyectos, trayectoria, podcasts y servicios de tecnología."
	/>
	<link rel="canonical" href="https://www.saavedratech.dev/" />
	{@html jsonLd}
</svelte:head>

<Navbar />
<main id="main-content">
	<Presentation socials={data.socials} />
	<Projects />
	<Jobs jobs={data.jobs} />
	<Services />
	<Podcast podcasts={data.podcasts} techs={data.techs} />
	<Skills skills={data.skills} techs={data.techs} />
	<Faq />
	<ContactCta />
</main>
<Footer socials={data.socials} />
