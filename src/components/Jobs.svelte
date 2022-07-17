<script>
    export let jobs;
</script>


<div class="mx-auto max-w-screen-lg px-3 py-6">
    
	<div class="mb-6 text-2xl font-bold">
		My <span class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent"> Jobs </span>
	</div>

    <div class="grid grid-cols-3 gap-4">
        {#each jobs as job}
            <div class="items-center gap-x-8 rounded-md bg-slate-800 p-3">
                <div>
                    <div class="flex flex-col items-center gap-y-2 md:flex-row">
                        <a class="hover:text-cyan-400" href="">
                            <div class="text-xl font-semibold">Project 1</div>
                        </a>
                    </div>
                    <p class="mt-3 text-gray-400">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse bibendum. Nunc non
                        posuere consectetur, justo erat semper enim, non hendrerit dui odio id enim.
                    </p>
                    <div class="flex flex-col items-center gap-y-2 md:flex-row">
                        <div class="ml-3 flex gap-2">
                            <div class="rounded-md px-2 py-1 text-xs font-semibold bg-fuchsia-400 text-fuchsia-900">
                                Astro.js
                            </div>
                            <div class="rounded-md px-2 py-1 text-xs font-semibold bg-lime-400 text-lime-900">
                                Web design
                            </div>
                            <div class="rounded-md px-2 py-1 text-xs font-semibold bg-sky-400 text-sky-900">
                                Tailwind.css
                            </div>
                            <div class="rounded-md px-2 py-1 text-xs font-semibold bg-rose-400 text-rose-900">
                                TypeScript
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        {/each}
    </div>


    
</div>
