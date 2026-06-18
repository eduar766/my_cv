<script>
    import "../app.css";
    let showBackToTop = false;

    function handleScroll() {
        showBackToTop = window.scrollY > 400;
    }
</script>

<svelte:window on:scroll={handleScroll}/>

<div class="bg-slate-900 text-gray-100 min-h-screen justify-between">
    <slot />
</div>

{#if showBackToTop}
    <button
        on:click={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
        class="fixed bottom-6 right-6 z-50 rounded-full bg-sky-500 p-3 text-white shadow-lg transition-all hover:bg-sky-400 hover:shadow-xl"
        aria-label="Back to top"
    >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z" clip-rule="evenodd" />
        </svg>
    </button>
{/if}
