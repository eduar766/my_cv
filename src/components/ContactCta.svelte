<script>
    import CalendlyButton from './CalendlyButton.svelte';
</script>

<section id="contact" class="mx-auto max-w-screen-lg px-3 py-12 md:py-16 animate-fade-in">
    <div class="rounded-lg bg-slate-800 px-6 py-10 text-center md:px-12">
        <h2 class="text-2xl font-bold">
            ¿Necesitas ayuda con tu <span class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent">infraestructura</span>?
        </h2>
        <p class="mx-auto mt-3 max-w-xl text-gray-300">
            Conversemos 30 minutos sin compromiso sobre tu arquitectura, tus costos en AWS o cómo acelerar a tu equipo con IA.
        </p>
        <div class="mt-6 flex justify-center">
            <CalendlyButton label="Agendar una llamada" variant="primary" />
        </div>
    </div>
</section>
