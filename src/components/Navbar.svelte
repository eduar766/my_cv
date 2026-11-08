<script>
	import Logo from './Logo.svelte';
	let menuOpen = false;
	const links = [
		['/#projects', 'Proyectos'],
		['/#experience', 'Experiencia'],
		['/#services', 'Servicios'],
		['/#podcasts', 'Podcasts']
	];
</script>

<a href="#main-content" class="skip-link">Saltar al contenido</a>
<header class="site-header">
	<div class="nav-inner">
		<a href="/" aria-label="SaavedraTech — Inicio" class="brand">
			<Logo class="h-9 w-9" />
			<span
				>Saavedra<span class="text-sky-400">Tech</span><small>El espacio de Eduardo Saavedra</small
				></span
			>
		</a>
		<button
			class="menu-toggle"
			aria-expanded={menuOpen}
			aria-controls="main-navigation"
			on:click={() => (menuOpen = !menuOpen)}>{menuOpen ? 'Cerrar ✕' : 'Menú ☰'}</button
		>
		<nav id="main-navigation" class:menu-open={menuOpen} aria-label="Navegación principal">
			{#each links as [href, label]}
				<a {href} on:click={() => (menuOpen = false)}>{label}</a>
			{/each}
			<a href="/#contact" class="nav-contact" on:click={() => (menuOpen = false)}
				>Contacto <span aria-hidden="true">↗</span></a
			>
		</nav>
	</div>
</header>
