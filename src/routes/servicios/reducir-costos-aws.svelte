<script context="module">
    export const prerender = true;
</script>

<script>
    import Navbar from '../../components/Navbar.svelte';
    import Footer from '../../components/Footer.svelte';
    import CalendlyButton from '../../components/CalendlyButton.svelte';
    import data from '../../eduardo.json';

    const SITE = "https://www.saavedratech.dev";
    const PAGE = `${SITE}/servicios/reducir-costos-aws`;

    const faqs = [
        {
            question: '¿Cuánto se puede reducir la factura de AWS?',
            answer: 'En cuentas sin optimizar es habitual encontrar ahorros del 20% al 40%. Las fuentes más comunes son instancias sobredimensionadas, ausencia de Savings Plans o Reserved Instances, NAT Gateways mal ubicados, almacenamiento sin políticas de ciclo de vida y recursos huérfanos que nadie apagó.'
        },
        {
            question: '¿Optimizar costos significa perder rendimiento o disponibilidad?',
            answer: 'No. La optimización bien hecha elimina desperdicio, no capacidad: se dimensiona según el uso real medido, se mantienen los márgenes de seguridad y los cambios se aplican por fases con métricas de control.'
        },
        {
            question: '¿Qué son los Savings Plans de AWS?',
            answer: 'Son compromisos de uso (1 o 3 años) a cambio de descuentos de hasta 72% sobre el precio on-demand. Elegir entre Savings Plans, Reserved Instances y Spot depende del patrón de uso de cada workload; parte del trabajo es armar esa combinación.'
        },
        {
            question: '¿Cómo se mide el resultado?',
            answer: 'Con la propia facturación de AWS: se define la línea base con Cost Explorer y CUR (Cost and Usage Report), se etiquetan los recursos y se compara la factura antes y después de cada fase.'
        }
    ];

    const structuredData = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "@id": `${PAGE}#service`,
                "name": "Optimización de costos AWS",
                "serviceType": "FinOps / Optimización de costos cloud",
                "url": PAGE,
                "description": "Reducción de la factura de AWS mediante right-sizing, Savings Plans, revisión de NAT Gateways, políticas de almacenamiento y eliminación de recursos huérfanos. Ahorros habituales del 20% al 40% en cuentas sin optimizar.",
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
                    { "@type": "ListItem", "position": 2, "name": "Reducir costos AWS", "item": PAGE }
                ]
            }
        ]
    };

    const jsonLd = `<script type="application/ld+json">${JSON.stringify(structuredData)}${'<'}/script>`;
</script>

<svelte:head>
    <title>Reducir costos AWS: optimización de factura cloud | Eduardo Saavedra</title>
    <meta name="description" content="Optimización de costos AWS para empresas de Chile y LATAM: right-sizing, Savings Plans, NAT Gateways y recursos huérfanos. Ahorros habituales del 20% al 40% sin perder rendimiento." />
    <link rel="canonical" href="https://www.saavedratech.dev/servicios/reducir-costos-aws" />
    {@html jsonLd}
</svelte:head>

<Navbar socials={data.socials}/>

<main class="mx-auto max-w-screen-md px-3 py-12 md:py-16">
    <nav class="mb-6 text-sm text-gray-400" aria-label="Breadcrumb">
        <a href="/" class="hover:text-white">Inicio</a> <span aria-hidden="true">/</span> Reducir costos AWS
    </nav>

    <h1 class="text-3xl font-bold md:text-4xl">
        Reducir <span class="bg-gradient-to-br from-sky-500 to-cyan-400 bg-clip-text text-transparent">costos AWS</span> sin sacrificar rendimiento
    </h1>

    <p class="mt-6 text-lg leading-8 text-gray-300">
        La optimización de costos AWS consiste en eliminar el desperdicio de una cuenta cloud —
        instancias sobredimensionadas, recursos huérfanos, tráfico mal enrutado, almacenamiento sin políticas —
        sin reducir capacidad ni disponibilidad. En cuentas que nunca han pasado por este proceso,
        <strong class="text-gray-100">los ahorros habituales van del 20% al 40% de la factura mensual</strong>.
    </p>

    <h2 class="mt-10 text-2xl font-bold">Dónde se esconde el gasto</h2>
    <ul class="mt-4 list-disc space-y-2 pl-5 text-gray-300">
        <li><strong class="text-gray-100">Right-sizing:</strong> instancias EC2 y RDS dimensionadas "por si acaso" que usan una fracción de su capacidad.</li>
        <li><strong class="text-gray-100">Sin compromisos de uso:</strong> pagar precio on-demand por workloads estables que califican para Savings Plans o Reserved Instances (descuentos de hasta 72%).</li>
        <li><strong class="text-gray-100">NAT Gateways:</strong> el clásico — tráfico entre AZs o hacia S3/DynamoDB que cruza NAT Gateways en vez de usar VPC Endpoints.</li>
        <li><strong class="text-gray-100">Almacenamiento:</strong> snapshots antiguos, volúmenes EBS sin adjuntar, buckets S3 sin políticas de ciclo de vida ni Intelligent-Tiering.</li>
        <li><strong class="text-gray-100">Recursos huérfanos:</strong> ambientes de prueba, load balancers y Elastic IPs que nadie apagó.</li>
        <li><strong class="text-gray-100">Arquitectura:</strong> a veces el mayor ahorro es estructural — pasar workloads intermitentes a serverless o consolidar clusters subutilizados.</li>
    </ul>

    <h2 class="mt-10 text-2xl font-bold">Cómo trabajo</h2>
    <ol class="mt-4 list-decimal space-y-3 pl-5 text-gray-300">
        <li><strong class="text-gray-100">Línea base:</strong> análisis de Cost Explorer y CUR para saber exactamente qué gasta cada servicio, ambiente y equipo.</li>
        <li><strong class="text-gray-100">Quick wins primero:</strong> recursos huérfanos y right-sizing evidente — ahorro en la primera factura.</li>
        <li><strong class="text-gray-100">Compromisos de uso:</strong> plan de Savings Plans / Reserved Instances según el patrón real de cada workload.</li>
        <li><strong class="text-gray-100">Cambios estructurales:</strong> VPC Endpoints, políticas de almacenamiento y ajustes de arquitectura, aplicados por fases con métricas de control.</li>
        <li><strong class="text-gray-100">Visibilidad permanente:</strong> etiquetado, presupuestos y alertas para que el gasto no vuelva a crecer a ciegas.</li>
    </ol>

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
        <h2 class="text-xl font-bold">¿Tu factura de AWS crece más rápido que tu negocio?</h2>
        <p class="mx-auto mt-2 max-w-md text-gray-300">En 30 minutos revisamos tu caso y te digo dónde están los ahorros más probables.</p>
        <div class="mt-5 flex justify-center">
            <CalendlyButton label="Agendar diagnóstico gratuito" variant="primary" />
        </div>
    </div>
</main>

<Footer socials={data.socials}/>
