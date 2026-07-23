<script>
    import Icon from '@iconify/svelte';
    import CalendlyButton from './CalendlyButton.svelte';

    const services = [
        {
            title: 'Revisión de arquitectura AWS',
            href: '/servicios/revision-arquitectura-aws',
            icon: 'mdi:aws',
            description:
                'Auditoría práctica de tu cuenta AWS enfocada en estabilidad, costo y seguridad. No es un checklist genérico: revisamos lo que realmente corre en producción.',
            scope: [
                'Arquitectura actual y dependencias críticas',
                'Costos y oportunidades de optimización inmediata',
                'Seguridad, networking y cumplimiento básico',
                'Cuellos de botella y riesgos de escalabilidad'
            ],
            deliverables: [
                'Informe priorizado de hallazgos y riesgos',
                'Diagrama actualizado de tu arquitectura',
                'Plan de acción por fases con impacto estimado',
                'Sesión de 60 min para revisar resultados'
            ],
            highlight: true
        },
        {
            title: 'Aceleración con IA',
            icon: 'mdi:robot',
            description:
                'Prototipos funcionales en días, no meses. Uso agentes e IA para automatizar flujos internos, acelerar desarrollo y reducir Time to Market.',
            scope: [
                'Prototipos de herramientas core con IA',
                'Automatización de procesos internos',
                'Asistentes y agentes para equipos técnicos'
            ],
            deliverables: [
                'MVP funcional en pocas semanas',
                'Integración con tu stack actual',
                'Documentación y handover al equipo'
            ],
            highlight: false
        },
        {
            title: 'Liderazgo técnico fractional',
            href: '/servicios/liderazgo-tecnico-fractional',
            icon: 'mdi:account-tie',
            description:
                'Technical Lead a demanda para equipos que necesitan dirección técnica sin contratar a tiempo completo.',
            scope: [
                'Diseño y revisión de arquitectura',
                'Mentoría del equipo de desarrollo',
                'Definición de procesos y buenas prácticas'
            ],
            deliverables: [
                'Reuniones semanales de seguimiento',
                'Decisiones técnicas documentadas',
                'Roadmap y priorización de deuda técnica'
            ],
            highlight: false
        }
    ];
</script>

<section id="services" class="mx-auto max-w-screen-lg px-3 py-12 md:py-16 animate-fade-in">
    <h2 class="mb-2 text-2xl font-bold">
        Mis <span class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent">Servicios</span>
    </h2>
    <p class="mb-6 text-gray-400">
        Consultoría práctica para escalar infraestructura, reducir costos y acelerar entregas.
    </p>

    <div class="grid grid-cols-1 gap-4 md:grid-cols-3">
        {#each services as service}
            <article
                class="relative flex flex-col rounded-md bg-slate-800 p-5 {service.highlight
                    ? 'border-2 border-sky-500'
                    : ''}"
                aria-label={service.title}
            >
                {#if service.highlight}
                    <span
                        class="absolute -top-3 right-4 rounded-full bg-gradient-to-br from-sky-500 to-cyan-400 px-3 py-1 text-xs font-bold text-white"
                    >
                        Más solicitado
                    </span>
                {/if}

                <div class="mb-3 flex items-center gap-3">
                    <div class="rounded-md bg-slate-700 p-2">
                        <Icon icon={service.icon} class="h-7 w-7 text-sky-400" />
                    </div>
                    <h3 class="text-xl font-semibold">{service.title}</h3>
                </div>

                <p class="mb-4 text-sm text-gray-300">{service.description}</p>

                <div class="mb-4 flex-1">
                    <h4 class="mb-2 text-xs font-bold uppercase tracking-wide text-gray-400">Alcance</h4>
                    <ul class="space-y-1.5">
                        {#each service.scope as item}
                            <li class="flex items-start gap-2 text-sm text-gray-300">
                                <span class="mt-1 h-1.5 w-1.5 shrink-0 rounded-full bg-sky-400" />
                                {item}
                            </li>
                        {/each}
                    </ul>
                </div>

                <div class="mb-5">
                    <h4 class="mb-2 text-xs font-bold uppercase tracking-wide text-gray-400">Qué recibes</h4>
                    <ul class="space-y-1.5">
                        {#each service.deliverables as item}
                            <li class="flex items-start gap-2 text-sm text-gray-300">
                                <Icon icon="mdi:check-circle" class="mt-0.5 h-4 w-4 shrink-0 text-green-400" />
                                {item}
                            </li>
                        {/each}
                    </ul>
                </div>

                <div class="mt-auto flex flex-col gap-2">
                    {#if service.href}
                        <a href={service.href} class="text-center text-sm font-semibold text-sky-400 hover:text-sky-300">
                            Ver detalle del servicio →
                        </a>
                    {/if}
                    <CalendlyButton
                        label="Agendar una llamada"
                        variant="primary"
                        class="w-full"
                    />
                </div>
            </article>
        {/each}
    </div>

    <p class="mt-4 text-sm text-gray-400">
        ¿Solo te preocupa la factura? Mira cómo trabajo la
        <a href="/servicios/reducir-costos-aws" class="font-semibold text-sky-400 hover:text-sky-300">optimización de costos AWS →</a>
    </p>
</section>
