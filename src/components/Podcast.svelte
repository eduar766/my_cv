<script>
    export let podcasts;
    export let techs;
    import Icon from '@iconify/svelte';

    import badrequestphoto from '$lib/assets/badrequest2.png';
    import visitarobotica from '$lib/assets/visita.png';


</script>

<div class="mx-auto max-w-screen-lg px-3 py-6">
	<div class="mb-6 text-2xl font-bold">
		<div class="flex items-baseline justify-between">
			<div>
				Listen to my <span class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent">podcast</span>
			</div>
		</div>
	</div>
	<div class="grid grid-cols-1 gap-6 md:grid-cols-2">
        {#each podcasts as pod }
            <a class="hover:translate-y-1" href="">
                <div class="overflow-hidden rounded-md bg-slate-800">
                    <div class="aspect-w-3 aspect-h-2">
                        {#if pod.id === 1}
                        <img
                            class="object-cover object-center h-15 w-15"
                            src={badrequestphoto}
                            loading="lazy"
                            alt=""
                        />
                        {:else if pod.id === 2}
                            <img
                                class="object-cover object-center h-15 w-15"
                                src={visitarobotica}
                                loading="lazy"
                                alt=""
                            />
                        {/if}
                    </div>
                    <div class="px-3 pt-4 pb-6 text-center">
                        <h2 class="text-xl font-semibold">{pod.title}</h2>
                        <div class="mt-2 text-sm">
                            {pod.description}
                        </div>
                    </div>

                    <div class="flex flex-col items-center gap-y-2 my-5">
                        <div class="grid grid-cols-3 items-center md:grid-cols-3 ">
                            {#each pod.platform as podi }
                                {#each techs as t}
                                    {#if t.name === podi.title}
                                    <a href={podi.url}>
                                        <Icon icon={t.icon} class="h-10 w-10 hover:translate-y-1 m-3" loading="lazy"/>
                                    </a>
                                    {/if}        
                                {/each}
                            {/each}
                        </div>

                    </div>
                    

                    
                </div>
            </a>
            
        {/each}
	</div>
</div>
