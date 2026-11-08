<script>
	import '../app.css';
	import { page } from '$app/stores';
	$: isLazyCase = $page.url.pathname.replace(/\/$/, '') === '/proyectos/lazy-crm';
	$: shareTitle = isLazyCase
		? 'Cómo construí Lazy CRM — Eduardo Saavedra'
		: 'Eduardo Saavedra — Ingeniero y creador de productos';
	$: shareDescription = isLazyCase
		? 'Producto, arquitectura y decisiones detrás de un CRM para freelancers.'
		: 'Ingeniero, Technical Lead y creador de Futbocracy, Lazy CRM y Komorebi. Proyectos, trayectoria, podcasts y servicios.';
	$: shareImage =
		'https://www.saavedratech.dev/' +
		(isLazyCase ? 'projects/lazy-crm-preview.png' : 'og-image.png');
	let showBackToTop = false;

	function handleScroll() {
		showBackToTop = window.scrollY > 400;
	}
</script>

<svelte:head>
	<meta property="og:title" content={shareTitle} />
	<meta property="og:description" content={shareDescription} />
	<meta property="og:type" content={isLazyCase ? 'article' : 'profile'} />
	<meta
		property="og:url"
		content={'https://www.saavedratech.dev' + (isLazyCase ? '/proyectos/lazy-crm' : '/')}
	/>
	<meta property="og:image" content={shareImage} />
	<meta property="og:image:width" content={isLazyCase ? '1440' : '1200'} />
	<meta property="og:image:height" content={isLazyCase ? '1200' : '630'} />
	<meta name="twitter:title" content={shareTitle} />
	<meta name="twitter:description" content={shareDescription} />
	<meta name="twitter:image" content={shareImage} />
	{#if !isLazyCase}<meta property="profile:first_name" content="Eduardo" /><meta
			property="profile:last_name"
			content="Saavedra"
		/>{/if}
</svelte:head>

<svelte:window on:scroll={handleScroll} />

<div class="site-shell text-gray-100 min-h-screen justify-between">
	<slot />
</div>

{#if showBackToTop}
	<button
		on:click={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
		class="fixed bottom-6 right-6 z-50 rounded-full bg-sky-500 p-3 text-white shadow-lg transition-all hover:bg-sky-400 hover:shadow-xl"
		aria-label="Volver al inicio"
	>
		<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
			<path
				fill-rule="evenodd"
				d="M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z"
				clip-rule="evenodd"
			/>
		</svg>
	</button>
{/if}
