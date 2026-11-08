<script>
	import Icon from '@iconify/svelte';
	export let socials;
	const year = new Date().getFullYear();
</script>

<footer class="page-section site-footer">
	<div class="footer-inner">
		<div>
			<p>© {year} Eduardo Saavedra</p>
			<p class="footer-note">Ideas, código y cosas por construir.</p>
		</div>
		<nav class="footer-socials" aria-label="Redes sociales">
			{#each socials as social}<a
					href={social.url}
					target="_blank"
					rel="noopener noreferrer"
					aria-label={social.title}><Icon icon={social.icon} class="h-5 w-5" /></a
				>{/each}
		</nav>
		<a
			class="text-link"
			href="https://github.com/eduar766/my_cv"
			target="_blank"
			rel="noopener noreferrer">Ver el código ↗</a
		>
	</div>
</footer>
