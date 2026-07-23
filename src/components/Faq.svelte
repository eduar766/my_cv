<script>
    export let faqs = [
        {
            question: '¿Qué incluye una revisión de arquitectura AWS?',
            answer: 'Incluye el análisis de la arquitectura actual y sus dependencias críticas, revisión de costos con oportunidades de optimización inmediata, evaluación de seguridad y networking, y detección de cuellos de botella de escalabilidad. Entrego un informe priorizado, un diagrama actualizado de la arquitectura y un plan de acción por fases, más una sesión de 60 minutos para revisar resultados.'
        },
        {
            question: '¿Trabajas con empresas fuera de Chile?',
            answer: 'Sí. Estoy en Santiago de Chile y trabajo de forma remota con empresas de toda Latinoamérica, en español e inglés.'
        },
        {
            question: '¿Cuánto se puede reducir la factura de AWS?',
            answer: 'Depende del estado de la cuenta, pero en cuentas sin optimizar es habitual encontrar ahorros del 20% al 40% mediante right-sizing, Savings Plans, revisión de NAT Gateways y almacenamiento, y eliminación de recursos huérfanos. La revisión identifica los ahorros de mayor impacto primero.'
        },
        {
            question: '¿Qué es un Technical Lead fractional?',
            answer: 'Es un líder técnico senior que trabaja con tu equipo algunas horas o días por semana: define arquitectura, revisa decisiones técnicas, mentorea a los desarrolladores y prioriza deuda técnica, sin el costo de una contratación a tiempo completo.'
        }
    ];
</script>

<section id="faq" class="mx-auto max-w-screen-lg px-3 py-12 md:py-16 animate-fade-in">
    <h2 class="mb-6 text-2xl font-bold">
        Preguntas <span class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent">frecuentes</span>
    </h2>
    <div class="space-y-3">
        {#each faqs as faq}
            <details class="group rounded-md bg-slate-800 p-4">
                <summary class="cursor-pointer list-none font-semibold text-gray-100 marker:content-none flex items-center justify-between gap-3">
                    {faq.question}
                    <span class="shrink-0 text-sky-400 transition-transform group-open:rotate-45 text-xl leading-none" aria-hidden="true">+</span>
                </summary>
                <p class="mt-3 text-gray-300">{faq.answer}</p>
            </details>
        {/each}
    </div>
</section>
