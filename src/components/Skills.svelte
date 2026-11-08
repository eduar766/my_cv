<script>
	export let skills;
	export let techs;
	import Icon from '@iconify/svelte';

	function getIcon(name) {
		const match = techs.find((t) => t.name === name);
		return match ? match.icon : '';
	}
</script>

<section id="skills" class="page-section">
	<div class="section-heading">
		<div>
			<p class="eyebrow">Mi caja de herramientas</p>
			<h2>Tecnología con propósito<span class="text-sky-400">.</span></h2>
		</div>
		<p>
			Elijo las herramientas según el problema: cloud, backend, automatización e inteligencia
			artificial.
		</p>
	</div>
	<div class="grid grid-cols-1 gap-4 md:grid-cols-3">
		{#each skills as skill}
			<div class="skill-group">
				<h3 class="text-lg font-semibold text-sky-400">{skill.category}</h3>
				<div class="mt-3 flex flex-wrap gap-2">
					{#each skill.items as item}
						{#if getIcon(item)}
							<div
								class="flex items-center gap-1 rounded-md border border-slate-700/70 px-2 py-1"
								title={item}
							>
								<Icon icon={getIcon(item)} class="h-5 w-5" loading="lazy" />
								<span class="text-xs text-gray-300"
									>{item === 'aws' ? 'AWS' : item === 'ai' ? 'IA' : item}</span
								>
							</div>
						{/if}
					{/each}
				</div>
			</div>
		{/each}
	</div>
</section>
