<script>
	import Icon from '@iconify/svelte';
	const services = [
		{
			title: 'Arquitectura AWS',
			icon: 'mdi:aws',
			description:
				'Una mirada práctica a tu infraestructura para identificar riesgos y preparar el siguiente paso.',
			points: [
				'Estabilidad, seguridad y escalabilidad',
				'Informe priorizado y plan de acción',
				'Oportunidades de optimización de costos'
			],
			href: '/servicios/revision-arquitectura-aws'
		},
		{
			title: 'Aceleración con IA',
			icon: 'mdi:robot',
			description:
				'De una idea a un prototipo funcional, integrando IA donde aporte valor a tu equipo.',
			points: [
				'Prototipos y herramientas internas',
				'Automatización de procesos',
				'Integración y transferencia al equipo'
			],
			href: '/#contact'
		},
		{
			title: 'Liderazgo técnico',
			icon: 'mdi:account-tie',
			description:
				'Dirección técnica a demanda para equipos que necesitan experiencia y acompañamiento.',
			points: [
				'Diseño y decisiones de arquitectura',
				'Mentoría y buenas prácticas',
				'Roadmap y priorización técnica'
			],
			href: '/servicios/liderazgo-tecnico-fractional'
		}
	];
</script>

<section id="services" class="page-section">
	<div class="section-heading">
		<div>
			<p class="eyebrow">Trabajemos juntos</p>
			<h2>Cómo puedo ayudarte<span class="text-sky-400">.</span></h2>
		</div>
		<p>También pongo mi experiencia al servicio de otros equipos, proyectos y desafíos.</p>
	</div>
	<div class="service-grid">
		{#each services as service}
			<article class="service-card">
				<Icon icon={service.icon} class="h-7 w-7 text-sky-400" />
				<h3>{service.title}</h3>
				<p>{service.description}</p>
				<ul>
					{#each service.points as point}<li>{point}</li>{/each}
				</ul>
				<a class="text-link" href={service.href}
					>{service.title === 'Aceleración con IA' ? 'Hablemos de tu idea' : 'Conocer el servicio'}
					<span aria-hidden="true">→</span></a
				>
			</article>
		{/each}
	</div>
	<p class="service-footnote">
		¿Tu foco está en la factura cloud? <a class="text-link" href="/servicios/reducir-costos-aws"
			>Optimización de costos AWS →</a
		>
	</p>
</section>
