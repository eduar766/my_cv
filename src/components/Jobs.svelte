<script>
    export let jobs;
    export let techs;
    import Icon from '@iconify/svelte';

    let expanded = {};

    function toggle(id) {
        expanded[id] = !expanded[id];
        expanded = expanded;
    }
</script>

<section id="experience" class="mx-auto max-w-screen-lg px-3 py-12 md:py-16 animate-fade-in">
	<h2 class="mb-2 text-2xl font-bold">
		Mi <span class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent"> Experiencia </span>
	</h2>
    <p class="mb-6 text-gray-400">
        Resultados concretos que respaldan la oferta de consultoría.
    </p>

    <div class="mb-6 grid grid-cols-1 gap-3 md:grid-cols-2">
        <div class="rounded-md bg-slate-800 p-4">
            <p class="text-2xl font-bold text-sky-400">Nivel nacional</p>
            <h3 class="mt-1 font-semibold text-gray-200">Cencosud</h3>
            <p class="text-sm text-gray-300">Lideré Moncap, sistema de gestión de capacidades a nivel nacional para supermercados.</p>
        </div>
        <div class="rounded-md bg-slate-800 p-4">
            <p class="text-2xl font-bold text-sky-400">5 países</p>
            <h3 class="mt-1 font-semibold text-gray-200">Cencosud</h3>
            <p class="text-sm text-gray-300">Lideré el lanzamiento de Balancer, solución de optimización de ventanas horarias escalada a 5 países.</p>
        </div>
        <div class="rounded-md bg-slate-800 p-4">
            <p class="text-2xl font-bold text-sky-400">-40% Time to Market</p>
            <h3 class="mt-1 font-semibold text-gray-200">BK Servicios Financieros</h3>
            <p class="text-sm text-gray-300">Reduje el Time to Market al menos un 40% usando IA para prototipado de herramientas core.</p>
        </div>
        <div class="rounded-md bg-slate-800 p-4">
            <p class="text-2xl font-bold text-sky-400">Integración Salesforce</p>
            <h3 class="mt-1 font-semibold text-gray-200">BK Servicios Financieros</h3>
            <p class="text-sm text-gray-300">Dirigí la integración de sistemas legado con Salesforce para Crediautos.</p>
        </div>
    </div>

    <div class="grid grid-cols-1 gap-4 md:grid-cols-3">
        {#each jobs as job}
            <article class="items-center gap-x-8 rounded-md bg-slate-800 p-3" aria-label={`${job.company} - ${job.jobTitle}`}>
                <div>
                    <div class="flex flex-col gap-y-2">
                        <div class="flex items-center justify-between">
                            <h3 class="text-xl font-semibold">{job.company}</h3>
                            {#if job.endDate === "Presente"}
                                <span class="rounded-full bg-green-500 px-2 py-0.5 text-xs font-bold text-white">Presente</span>
                            {/if}
                        </div>
                        <div class="flex flex-wrap gap-2 mt-1">
                            <span class="rounded-md bg-sky-900 px-2 py-0.5 text-xs font-medium text-sky-200">{job.startDate} → {job.endDate}</span>
                            <span class="rounded-md bg-slate-700 px-2 py-0.5 text-xs font-medium text-gray-200">{job.jobTitle}</span>
                            {#if job.place}
                                <span class="rounded-md bg-slate-700 px-2 py-0.5 text-xs font-medium text-gray-200">{job.place}</span>
                            {/if}
                        </div>
                    </div>
                    <p class="mt-3 text-sm text-gray-400">
                        {#if !expanded[job.id] && job.description.length > 150}
                            {job.description.slice(0, 150)}...
                            <button class="text-sky-400 hover:text-sky-300 ml-1" on:click|preventDefault={() => toggle(job.id)}>Leer más</button>
                        {:else}
                            {job.description}
                            {#if job.description.length > 150}
                                <button class="text-sky-400 hover:text-sky-300 ml-1" on:click|preventDefault={() => toggle(job.id)}>Ver menos</button>
                            {/if}
                        {/if}
                    </p>
                    <div class="mt-4 text-sm font-semibold">
                        Tecnologías <span class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent"> utilizadas </span>
                    </div>

                    <div class="flex flex-col items-center gap-y-2 md:flex-row my-3">
                        <div class="grid grid-cols-5 md:grid-cols-6">
                            {#each job.technologies as jb }
                                {#each techs as t}
                                    {#if t.name === jb}
                                        <Icon icon={t.icon} class="h-8 w-8 transition-transform hover:-translate-y-1" loading="lazy"/>
                                    {/if}        
                                {/each}
                            {/each}
                        </div>
                    </div>
                </div>
            </article>
        {/each}
    </div>
</section>
