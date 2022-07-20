<script>
    export let jobs;
    export let techs;
    import Icon from '@iconify/svelte';
</script>


<div class="mx-auto max-w-screen-lg px-3 py-6">
    
	<div class="mb-6 text-2xl font-bold">
		My <span class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent"> Experience </span>
	</div>

    <div class="grid grid-cols-1 gap-4 md:grid-cols-3">
        {#each jobs as job}
            <div class="items-center gap-x-8 rounded-md bg-slate-800 p-3 w">
                <div>
                    <div class="flex flex-col gap-y-2 ">
                        <a class="hover:text-cyan-400" href="/">
                            <div class="text-xl font-semibold">{job.company}</div>
                        </a>
                        <p class="mt-1 text-xs">
                            <span class="font-bold text-sky-500">Start:</span> {job.startDate}
                            <span class="font-bold text-sky-500">End:</span> {job.endDate}
                        </p>
                        <p class="mt-1 text-xs">
                            <span class="font-bold text-sky-500">Job:</span> {job.jobTitle}
                        </p>
                        <p class="mt-1 text-xs">
                            {#if job.place}
                                <span class="font-bold text-sky-500">Place:</span> {job.place}
                            {/if} 
                        </p>
                    </div>
                    <p class="mt-3 text-gray-400">
                        {job.description}
                    </p>
                    <div class="text-xl font-semibold">
                        Used <span class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent"> Technologies </span>
                    </div>

                    <div class="flex flex-col items-center gap-y-2 md:flex-row my-5">
                        <div class="grid grid-cols-5 md:grid-cols-6 ">
                            {#each job.technologies as jb }
                                {#each techs as t}
                                    {#if t.name === jb}
                                        <Icon icon={t.icon} class="h-10 w-10 hover:translate-y-1" loading="lazy"/>
                                    {/if}        
                                {/each}
                            {/each}
                        </div>
                    </div>
                </div>
            </div>
        {/each}
    </div>


    
</div>
