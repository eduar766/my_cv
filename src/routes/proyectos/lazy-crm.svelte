<script context="module">
	export const prerender = true;
</script>

<script>
	import Navbar from '../../components/Navbar.svelte';
	import Footer from '../../components/Footer.svelte';
	import data from '../../eduardo.json';
	const devArticle =
		'https://dev.to/eduar766/building-a-crm-for-freelancers-architecture-decisions-behind-lazy-crm-19m';
	const mediumArticle =
		'https://medium.com/@eduar766/you-dont-need-salesforce-you-need-a-spreadsheet-that-doesn-t-suck-7f41103370dd';
	const decisions = [
		{
			number: '01',
			title: 'Separar descubrimiento y uso diario',
			problem:
				'La página pública necesita ser encontrable. El CRM necesita responder a formularios, navegación y movimientos de tarjetas.',
			choice:
				'Usé Next.js para la landing y React con Vite para la aplicación, con una API independiente en NestJS.',
			tradeoff:
				'Cada aplicación se construye por separado. Mantengo más de un proyecto, a cambio de adaptar cada uno a su función.'
		},
		{
			number: '02',
			title: 'Distinguir los datos del servidor del estado de la interfaz',
			problem:
				'Clientes, oportunidades y facturas vienen de la API. Los pasos de un formulario pertenecen a la interacción local.',
			choice:
				'TanStack Query gestiona consultas y actualizaciones; Zustand guarda el estado local del asistente de facturación.',
			tradeoff:
				'Hay dos herramientas de estado, con responsabilidades distintas. Al mover una oportunidad, la interfaz responde primero y revierte el cambio si la API falla.'
		},
		{
			number: '03',
			title: 'Organizar para avanzar sin perder claridad',
			problem:
				'Un producto construido por una persona necesita estructura mantenible y poca carga operativa.',
			choice:
				'Organicé NestJS por dominios de negocio y usé Prisma con PostgreSQL administrado en Neon. Los tres proyectos conviven en un repositorio y se construyen de forma independiente.',
			tradeoff:
				'No hay paquetes compartidos ni contratos de tipos de extremo a extremo. Esa simplicidad ha implicado desajustes entre los tipos del frontend y las respuestas de la API.'
		}
	];
	const jsonLd = `<script type="application/ld+json">${JSON.stringify({
		'@context': 'https://schema.org',
		'@type': 'Article',
		headline: 'Lazy CRM: de una necesidad propia a un producto funcional',
		description:
			'Un caso de estudio sobre producto, arquitectura y decisiones al construir un CRM para freelancers.',
		inLanguage: 'es',
		author: { '@type': 'Person', name: 'Eduardo Saavedra', url: 'https://www.saavedratech.dev/' },
		mainEntityOfPage: 'https://www.saavedratech.dev/proyectos/lazy-crm',
		image: 'https://www.saavedratech.dev/projects/lazy-crm-preview.png',
		citation: [devArticle, mediumArticle]
	})}${'<'}/script>`;
</script>

<svelte:head>
	<title>Cómo construí Lazy CRM — Eduardo Saavedra</title>
	<meta
		name="description"
		content="De una necesidad como freelancer a un CRM funcional: el problema, las decisiones de producto, la arquitectura y los compromisos detrás de Lazy CRM."
	/>
	<link rel="canonical" href="https://www.saavedratech.dev/proyectos/lazy-crm" />
	{@html jsonLd}
</svelte:head>

<Navbar />
<main id="main-content" class="case-page">
	<nav class="case-breadcrumb" aria-label="Ruta de navegación">
		<a href="/#projects">Proyectos</a><span aria-hidden="true">/</span><span>Lazy CRM</span>
	</nav>
	<header class="case-hero">
		<p class="eyebrow">Caso de estudio · Producto propio</p>
		<h1>
			Lazy CRM.<br />De una necesidad propia a un
			<span class="text-sky-400">producto funcional.</span>
		</h1>
		<p class="case-intro">
			Cómo diseñé y construí una herramienta para que los profesionales independientes dediquen
			menos tiempo a administrar su negocio y más a su trabajo.
		</p>
		<div class="case-meta">
			<div><span>Mi papel</span><strong>Creador y desarrollador</strong></div>
			<div><span>Para quién</span><strong>Freelancers y pequeños negocios</strong></div>
			<div><span>El foco</span><strong>Clientes, oportunidades y facturas</strong></div>
		</div>
		<a
			class="button-primary"
			href="https://lazy-crm.com/es"
			target="_blank"
			rel="noopener noreferrer">Visitar Lazy CRM <span aria-hidden="true">↗</span></a
		>
	</header>
	<figure class="case-preview">
		<img
			src="/projects/lazy-crm-preview.png"
			alt="Página pública de Lazy CRM en español, con su propuesta de valor y una demostración del panel"
			width="1440"
			height="1200"
		/>
		<figcaption>
			Vista pública del producto. Las cifras de la demostración son ilustrativas.
		</figcaption>
	</figure>
	<nav class="case-index" aria-label="En este caso de estudio">
		<a href="#problema">El problema</a><a href="#producto">El producto</a><a href="#arquitectura"
			>La arquitectura</a
		><a href="#aprendizajes">Los aprendizajes</a>
	</nav>
	<section id="problema" class="case-section case-split">
		<div>
			<p class="eyebrow">01 · El punto de partida</p>
			<h2>Una necesidad que conocía de primera mano.</h2>
		</div>
		<div class="case-prose">
			<p>
				Mi experiencia como freelancer me acercó al problema: clientes, propuestas y facturas
				repartidos entre herramientas que exigen atención constante. Una hoja de cálculo puede
				quedarse corta; un CRM orientado a grandes equipos puede añadir demasiada complejidad.
			</p>
			<p>
				Las conversaciones con profesionales independientes me ayudaron a concentrar la propuesta en
				cuatro tareas: organizar clientes, seguir oportunidades, generar facturas y entender cómo va
				el negocio.
			</p>
			<p class="case-principle">
				La pregunta de producto: ¿cuál es la mínima estructura que ayuda a trabajar mejor cada día?
			</p>
		</div>
	</section>
	<section id="producto" class="case-section">
		<div class="section-heading">
			<div>
				<p class="eyebrow">02 · Diseñar alrededor del trabajo</p>
				<h2>Un recorrido conectado.</h2>
			</div>
			<p>El flujo comercial guía las funcionalidades y conecta la información entre cada paso.</p>
		</div>
		<ol class="product-flow">
			<li>
				<span>01</span>
				<h3>Registrar al cliente</h3>
				<p>Datos de contacto y notas para mantener el contexto de cada relación.</p>
			</li>
			<li>
				<span>02</span>
				<h3>Seguir la oportunidad</h3>
				<p>Un tablero visual: nueva, negociación, ganada o perdida.</p>
			</li>
			<li>
				<span>03</span>
				<h3>Preparar la factura</h3>
				<p>Partir de una oportunidad ganada, añadir conceptos y generar un PDF para compartir.</p>
			</li>
		</ol>
		<p class="case-flow-note">
			El panel reúne el avance frente a la meta mensual y el estado de las oportunidades. La
			aplicación también permite recibir leads mediante webhooks y trabajar en español o inglés.
		</p>
	</section>
	<section id="arquitectura" class="case-section">
		<p class="eyebrow">03 · Las decisiones detrás de la interfaz</p>
		<h2>Una arquitectura al servicio del producto.</h2>
		<p class="case-lead">
			Estas decisiones, documentadas en mi artículo técnico, separan la web pública, el uso diario
			del CRM y la lógica del negocio.
		</p>
		<figure class="architecture-map">
			<div class="architecture-clients">
				<div>
					<span>Descubrir</span><strong>Landing pública</strong><small>Next.js · next-intl</small>
				</div>
				<div>
					<span>Trabajar</span><strong>Aplicación CRM</strong><small
						>React · Vite · TypeScript</small
					>
				</div>
			</div>
			<div class="architecture-connection">
				Aplicación CRM <span aria-hidden="true">→</span> API
			</div>
			<div class="architecture-api">
				<span>Lógica de negocio</span><strong>NestJS</strong><small
					>Autenticación · Clientes · Oportunidades · Facturación</small
				>
			</div>
			<div class="architecture-connection" aria-hidden="true">↓</div>
			<div class="architecture-storage">
				<div><strong>PostgreSQL en Neon</strong><small>Acceso a datos con Prisma</small></div>
				<div><strong>Almacenamiento y correo</strong><small>PDFs y envío de facturas</small></div>
			</div>
			<figcaption>
				Esquema simplificado de responsabilidades; no representa la topología de despliegue.
			</figcaption>
		</figure>
		<div class="decision-list">
			{#each decisions as decision}<article class="decision">
					<span class="decision-number">{decision.number}</span>
					<div>
						<h3>{decision.title}</h3>
						<dl>
							<div>
								<dt>El problema</dt>
								<dd>{decision.problem}</dd>
							</div>
							<div>
								<dt>La decisión</dt>
								<dd>{decision.choice}</dd>
							</div>
							<div>
								<dt>El compromiso</dt>
								<dd>{decision.tradeoff}</dd>
							</div>
						</dl>
					</div>
				</article>{/each}
		</div>
	</section>
	<section id="aprendizajes" class="case-section case-split">
		<div>
			<p class="eyebrow">04 · Lo que revisaría al crecer</p>
			<h2>La simplicidad también tiene límites.</h2>
		</div>
		<div class="case-prose">
			<p>
				Los proyectos comparten repositorio, pero no una configuración de workspaces ni tipos
				compartidos. Esa elección reduce preparación inicial, aunque obliga a cuidar manualmente los
				contratos entre frontend y backend.
			</p>
			<p>
				Para un equipo mayor o una API más extensa, incorporaría generación de tipos desde OpenAPI o
				contratos compartidos. También evaluaría workspaces y una construcción coordinada de los
				proyectos.
			</p>
			<p class="case-principle">
				El aprendizaje: elegir una solución implica entender qué facilita hoy y qué habrá que
				revisar mañana.
			</p>
		</div>
	</section>
	<section class="case-section">
		<div class="section-heading">
			<div>
				<p class="eyebrow">05 · Del caso al producto</p>
				<h2>Lo que puedes explorar.</h2>
			</div>
			<p>
				El resultado es una herramienta que reúne el flujo comercial de un profesional
				independiente.
			</p>
		</div>
		<div class="case-outcome">
			<p>
				Gestión de clientes, tablero de oportunidades, facturación en PDF, metas mensuales, webhooks
				e interfaz bilingüe. Un producto donde las decisiones de experiencia y arquitectura
				responden al mismo objetivo: simplificar el trabajo diario.
			</p>
			<a
				class="button-primary"
				href="https://lazy-crm.com/es"
				target="_blank"
				rel="noopener noreferrer">Conocer el producto ↗</a
			>
		</div>
	</section>
	<section class="case-section case-reading">
		<p class="eyebrow">Escrito por mí</p>
		<h2>Dos perspectivas del mismo proyecto.</h2>
		<p class="case-lead">
			Este caso adapta al español las ideas de mis artículos originales. Puedes profundizar en ellos
			en inglés.
		</p>
		<div class="case-reading-grid">
			<a href={mediumArticle} target="_blank" rel="noopener noreferrer"
				><span>Producto · Medium · En inglés</span>
				<h3>Por qué construir un CRM para freelancers</h3>
				<p>El problema, el usuario y las funcionalidades que dan forma a Lazy CRM.</p>
				<strong>Leer artículo original ↗</strong></a
			><a href={devArticle} target="_blank" rel="noopener noreferrer"
				><span>Arquitectura · DEV.to · En inglés</span>
				<h3>Las decisiones técnicas detrás de Lazy CRM</h3>
				<p>La estructura del proyecto, el manejo del estado y los compromisos técnicos.</p>
				<strong>Leer artículo original ↗</strong></a
			>
		</div>
	</section>
	<div class="case-end">
		<a class="text-link" href="/#projects">← Volver a mis proyectos</a><a
			class="text-link"
			href="/#contact">Conversemos sobre tu proyecto →</a
		>
	</div>
</main>
<Footer socials={data.socials} />
