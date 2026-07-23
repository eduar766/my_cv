<script>
    import Navbar from '../components/Navbar.svelte';
    import Presentation from '../components/Presentation.svelte';
    import Services from '../components/Services.svelte';
    import Jobs from '../components/Jobs.svelte';
    import Skills from '../components/Skills.svelte';
    import Footer from '../components/Footer.svelte';
    import Podcast from '../components/Podcast.svelte';
    import ContactCta from '../components/ContactCta.svelte';

    import data from'../eduardo.json';

    const structuredData = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Eduardo Saavedra",
        "givenName": "Eduardo",
        "familyName": "Saavedra",
        "jobTitle": data.profession,
        "description": data.about,
        "url": "https://www.saavedratech.dev/",
        "sameAs": data.socials.map(s => s.url),
        "telephone": data.phone,
        "address": {
            "@type": "PostalAddress",
            "addressLocality": data.city,
            "addressCountry": data.country
        },
        "knowsAbout": data.techs.filter(t => t.name !== 'anchor' && t.name !== 'spotify' && t.name !== 'rss').map(t => t.name),
        "worksFor": {
            "@type": "Organization",
            "name": "BK Servicios Financieros"
        },
        "alumniOf": {
            "@type": "CollegeOrUniversity",
            "name": "UNEFA",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Anzoátegui",
                "addressCountry": "Venezuela"
            }
        }
    };

    const jsonLd = `<script type="application/ld+json">${JSON.stringify(structuredData)}${'<'}/script>`;
</script>

<svelte:head>
	<title>Eduardo Saavedra - Technical Lead & Consultor AWS</title>
	<meta name="description" content="Technical Lead con más de 10 años de experiencia en retail y fintech. Consultoría práctica: revisión de arquitectura AWS, aceleración con IA y liderazgo técnico fractional." />
	{@html jsonLd}
</svelte:head>

<main>
    <Navbar socials={data.socials}/>
    <Presentation
        about={data.about}
        socials={data.socials}
        headline="Ayudo a empresas a escalar su infraestructura AWS sin caídas ni sorpresas en la factura."
    />
    <Services />
    <Jobs jobs={data.jobs} techs={data.techs} />
    <Skills skills={data.skills} techs={data.techs} />
    <Podcast podcasts={data.podcasts} techs={data.techs}/>
    <ContactCta />
    <Footer socials={data.socials}/>
</main>