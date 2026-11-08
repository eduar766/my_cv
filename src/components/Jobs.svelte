<script>
	export let jobs;
</script>

<section id="experience" class="page-section">
	<div class="section-heading">
		<div>
			<p class="eyebrow">El recorrido detrás de lo que hago</p>
			<h2>Experiencia en el mundo real<span class="text-sky-400">.</span></h2>
		</div>
		<p>
			Más de una década construyendo sistemas y acompañando equipos en retail, fintech y desarrollo
			de productos.
		</p>
	</div>
	<div class="case-grid">
		<article class="case-study">
			<p class="eyebrow">Cencosud · Retail</p>
			<h3>De la operación nacional a <span class="text-sky-400">5 países.</span></h3>
			<p>
				Lideré Moncap, una plataforma de gestión de capacidades para supermercados a nivel nacional,
				y el lanzamiento de Balancer, una solución de ventanas horarias escalada a cinco países.
			</p>
			<span class="case-label">Liderazgo técnico · Sistemas a escala</span>
		</article>
		<article class="case-study">
			<p class="eyebrow">BK Servicios Financieros · Fintech</p>
			<h3>Prototipos con IA, <span class="text-sky-400">40% menos Time to Market.</span></h3>
			<p>
				Incorporé agentes de IA al prototipado de herramientas core y dirigí la integración de
				sistemas legado con Salesforce para Crediautos.
			</p>
			<span class="case-label">Inteligencia artificial · Integraciones</span>
		</article>
	</div>
	<div class="timeline">
		{#each jobs as job, index}
			<article class="timeline-item">
				<div class="timeline-date">{job.startDate} — {job.endDate}</div>
				<div class="timeline-content">
					<h3>
						{job.company}
						{#if job.endDate === 'Presente'}<span class="current-job">Actual</span>{/if}
					</h3>
					<p class="timeline-role">{job.jobTitle}</p>
					<p class="timeline-place">{job.place}</p>
					{#if index < 2}<p class="timeline-summary">
							{index === 0
								? 'Arquitectura AWS, liderazgo de equipos e integración de plataformas financieras.'
								: 'Plataformas serverless y Kubernetes para operaciones de alta demanda.'}
						</p>{/if}
					<details>
						<summary>Ver experiencia <span aria-hidden="true">+</span></summary>
						<p>{job.description}</p>
						<p class="timeline-stack">{job.technologies.join(' · ')}</p>
					</details>
				</div>
			</article>
		{/each}
	</div>
</section>
