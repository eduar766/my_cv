<script>
    export let skills;
    export let techs;
    import Icon from '@iconify/svelte';

    function getIcon(name) {
        const match = techs.find(t => t.name === name);
        return match ? match.icon : '';
    }
</script>

<div class="mx-auto max-w-screen-lg px-3 py-6 animate-fade-in">
    <div class="mb-6 text-2xl font-bold">
        My <span class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent"> Skills </span>
    </div>

    <div class="grid grid-cols-1 gap-4 md:grid-cols-3">
        {#each skills as skill}
            <div class="rounded-md bg-slate-800 p-4">
                <h3 class="text-lg font-semibold text-sky-400">{skill.category}</h3>
                <div class="mt-3 flex flex-wrap gap-2">
                    {#each skill.items as item}
                        {#if getIcon(item)}
                            <div class="flex items-center gap-1 rounded-md bg-slate-700 px-2 py-1" title={item}>
                                <Icon icon={getIcon(item)} class="h-5 w-5" loading="lazy"/>
                                <span class="text-xs text-gray-300">{item}</span>
                            </div>
                        {/if}
                    {/each}
                </div>
            </div>
        {/each}
    </div>
</div>
