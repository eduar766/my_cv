<script>
	const projects = [
		{
			name: 'Futbocracy',
			category: 'Simulación & estrategia',
			logo: '/projects/futbocracy.png',
			url: 'https://futbocracy.com/',
			description:
				'Un simulador donde gobiernas una liga de fútbol: defines las reglas, administras recursos y construyes tu legado como comisionado.',
			detail: 'Los clubes juegan. Tú decides cómo crece la competición.',
			theme: 'football'
		},
		{
			name: 'Lazy CRM',
			category: 'Productividad & negocio',
			logo: '/projects/lazy-crm.png',
			url: 'https://lazy-crm.com/',
			description:
				'Un CRM minimalista para freelancers y pequeños negocios. Clientes, oportunidades comerciales y facturas, en un solo lugar.',
			detail: 'Menos administración. Más tiempo para tu trabajo.',
			theme: 'crm'
		},
		{
			name: 'Komorebi',
			category: 'Tecnología para psicólogos',
			logo: '/projects/komorebi.svg',
			url: 'https://trykomorebi.com/',
			description:
				'Una plataforma para psicólogos que conecta pacientes, herramientas de evaluación, seguimiento clínico y asistencia con IA.',
			detail: 'Herramientas conectadas para dar continuidad a la consulta.',
			theme: 'clinical'
		}
	];
</script>

<section id="projects" class="page-section">
	<div class="section-heading">
		<div>
			<p class="eyebrow">De la idea al producto</p>
			<h2>Productos que he creado<span class="text-sky-400">.</span></h2>
		</div>
		<p>
			Mi forma de aprender, explorar y resolver problemas: construir soluciones que se pueden usar.
		</p>
	</div>
	<div class="project-grid">
		{#each projects as project, index}
			<article class="project-card">
				<div class="project-art {project.theme}">
					<span class="project-number">0{index + 1}</span><img
						src={project.logo}
						alt="Logo de {project.name}"
						width="88"
						height="88"
						loading="lazy"
					/><span class="project-category">{project.category}</span>
				</div>
				<div class="project-body">
					<p class="project-authorship">Creador y desarrollador</p>
					<h3>{project.name}</h3>
					<p>{project.description}</p>
					<p class="project-detail">{project.detail}</p>
					<a
						class="text-link"
						href={project.url}
						target="_blank"
						rel="noopener noreferrer"
						aria-label="Explorar {project.name} (abre en otra pestaña)"
						>Explorar proyecto <span aria-hidden="true">↗</span></a
					>
				</div>
			</article>
		{/each}
	</div>
</section>
