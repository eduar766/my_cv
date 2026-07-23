<script context="module">
    export const prerender = true;
</script>

<script>
    import Navbar from '../../components/Navbar.svelte';
    import Footer from '../../components/Footer.svelte';
    import CalendlyButton from '../../components/CalendlyButton.svelte';
    import data from '../../eduardo.json';

    const SITE = "https://www.saavedratech.dev";
    const PAGE = `${SITE}/servicios/liderazgo-tecnico-fractional`;

    const faqs = [
        {
            question: '¿Qué es un Technical Lead fractional?',
            answer: 'Es un líder técnico senior que trabaja con tu equipo de forma parcial — algunas horas o días por semana — en lugar de una contratación a tiempo completo. Aporta dirección de arquitectura, revisión de decisiones técnicas, mentoría y priorización de deuda técnica.'
        },
        {
            question: '¿En qué se diferencia de contratar un CTO o Tech Lead full-time?',
            answer: 'El costo y el compromiso: obtienes criterio senior cuando lo necesitas, sin un sueldo ejecutivo completo. Es ideal para equipos de 2 a 15 desarrolladores que todavía no justifican (o no encuentran) un líder técnico dedicado.'
        },
        {
            question: '¿Cuántas horas por semana requiere?',
            answer: 'Los formatos habituales van de 4 a 16 horas semanales: reuniones de seguimiento, revisión de arquitectura y PRs críticos, sesiones de mentoría y disponibilidad asíncrona para decisiones técnicas.'
        },
        {
            question: '¿Trabajas de forma remota?',
            answer: 'Sí, trabajo remoto desde Santiago de Chile con empresas de toda Latinoamérica, en español e inglés.'
        }
    ];

    const structuredData = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "@id": `${PAGE}#service`,
                "name": "Liderazgo técnico fractional",
                "serviceType": "Fractional Technical Lead / CTO",
                "url": PAGE,
                "description": "Technical Lead a demanda para equipos que necesitan dirección técnica sin contratar a tiempo completo: diseño de arquitectura, mentoría del equipo, procesos y priorización de deuda técnica.",
                "provider": {
                    "@type": "Person",
                    "@id": `${SITE}/#eduardo`,
                    "name": "Eduardo Saavedra",
                    "jobTitle": "Consultor AWS & Technical Lead",
                    "url": SITE + "/",
                    "sameAs": data.socials.map(s => s.url)
                },
                "areaServed": [
                    { "@type": "Country", "name": "Chile" },
                    { "@type": "AdministrativeArea", "name": "Latinoamérica" }
                ],
                "availableLanguage": ["es", "en"]
            },
            {
                "@type": "FAQPage",
                "@id": `${PAGE}#faq`,
                "mainEntity": faqs.map(f => ({
                    "@type": "Question",
                    "name": f.question,
                    "acceptedAnswer": { "@type": "Answer", "text": f.answer }
                }))
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    { "@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/" },
                    { "@type": "ListItem", "position": 2, "name": "Liderazgo técnico fractional", "item": PAGE }
                ]
            }
        ]
    };

    const jsonLd = `<script type="application/ld+json">${JSON.stringify(structuredData)}${'<'}/script>`;
</script>

<svelte:head>
    <title>Technical Lead fractional en Chile y LATAM | Eduardo Saavedra</title>
    <meta name="description" content="Liderazgo técnico a demanda para equipos de desarrollo: arquitectura, mentoría, procesos y deuda técnica, sin contratar a tiempo completo. Remoto desde Santiago de Chile." />
    <link rel="canonical" href="https://www.saavedratech.dev/servicios/liderazgo-tecnico-fractional" />
    {@html jsonLd}
</svelte:head>

<Navbar socials={data.socials}/>

<main class="mx-auto max-w-screen-md px-3 py-12 md:py-16">
    <nav class="mb-6 text-sm text-gray-400" aria-label="Breadcrumb">
        <a href="/" class="hover:text-white">Inicio</a> <span aria-hidden="true">/</span> Liderazgo técnico fractional
    </nav>

    <h1 class="text-3xl font-bold md:text-4xl">
        Liderazgo técnico <span class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent">fractional</span>
    </h1>

    <p class="mt-6 text-lg leading-8 text-gray-300">
        Un Technical Lead fractional es un líder técnico senior que se integra a tu equipo de forma parcial —
        algunas horas o días por semana — para aportar <strong class="text-gray-100">dirección de arquitectura,
        mentoría y criterio técnico</strong>, sin el costo ni el compromiso de una contratación a tiempo completo.
    </p>

    <h2 class="mt-10 text-2xl font-bold">Para quién es</h2>
    <ul class="mt-4 list-disc space-y-2 pl-5 text-gray-300">
        <li>Startups con equipo de desarrollo pero sin líder técnico senior.</li>
        <li>Empresas donde el CTO está absorbido por gestión y el equipo necesita dirección técnica día a día.</li>
        <li>Equipos que enfrentan una decisión de arquitectura grande (migración a AWS, microservicios, escalamiento) y quieren criterio experimentado antes de comprometerse.</li>
        <li>Proyectos con deuda técnica acumulada que nadie prioriza.</li>
    </ul>

    <h2 class="mt-10 text-2xl font-bold">Qué hago como Technical Lead fractional</h2>
    <ul class="mt-4 list-disc space-y-2 pl-5 text-gray-300">
        <li>Diseño y revisión de arquitectura (especialidad: AWS, serverless, microservicios).</li>
        <li>Mentoría del equipo de desarrollo y revisión de PRs críticos.</li>
        <li>Definición de procesos y buenas prácticas: CI/CD, testing, observabilidad.</li>
        <li>Reuniones semanales de seguimiento y decisiones técnicas documentadas.</li>
        <li>Roadmap técnico y priorización de deuda técnica junto al negocio.</li>
    </ul>

    <h2 class="mt-10 text-2xl font-bold">Experiencia que respalda este servicio</h2>
    <p class="mt-4 text-gray-300">
        Más de 10 años en desarrollo de software y liderazgo técnico en retail y fintech. En Cencosud lideré
        equipos y plataformas a escala nacional e internacional (Moncap, Balancer en 5 países); hoy soy
        Technical Lead en BK Servicios Financieros, donde además reduje el Time to Market en al menos un 40%
        incorporando IA al ciclo de desarrollo.
    </p>

    <h2 class="mt-10 text-2xl font-bold">Preguntas frecuentes</h2>
    <div class="mt-4 space-y-3">
        {#each faqs as faq}
            <details class="group rounded-md bg-slate-800 p-4">
                <summary class="flex cursor-pointer list-none items-center justify-between gap-3 font-semibold text-gray-100 marker:content-none">
                    {faq.question}
                    <span class="shrink-0 text-xl leading-none text-sky-400 transition-transform group-open:rotate-45" aria-hidden="true">+</span>
                </summary>
                <p class="mt-3 text-gray-300">{faq.answer}</p>
            </details>
        {/each}
    </div>

    <div class="mt-12 rounded-lg bg-slate-800 px-6 py-8 text-center">
        <h2 class="text-xl font-bold">¿Tu equipo necesita dirección técnica?</h2>
        <p class="mx-auto mt-2 max-w-md text-gray-300">Conversemos 30 minutos sobre tu equipo y tus desafíos, sin compromiso.</p>
        <div class="mt-5 flex justify-center">
            <CalendlyButton label="Consultar disponibilidad" variant="primary" />
        </div>
    </div>
</main>

<Footer socials={data.socials}/>
