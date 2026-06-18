<script>
    import { onMount } from 'svelte';
    import Navbar from '../components/Navbar.svelte';
    import Presentation from '../components/Presentation.svelte';
    import Jobs from '../components/Jobs.svelte';
    import Skills from '../components/Skills.svelte';
    import Footer from '../components/Footer.svelte';
    import Podcast from '../components/Podcast.svelte';

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

    onMount(() => {
        const script = document.createElement('script');
        script.type = 'application/ld+json';
        script.textContent = JSON.stringify(structuredData);
        document.head.appendChild(script);
    });
</script>

<svelte:head>
	<title>Eduardo Saavedra - Technical Lead Senior & Software Engineer</title>
	<meta name="description" content="Eduardo Saavedra, Technical Lead Senior especializado en microservicios, AWS e IA. Más de 10 años liderando transformación digital en retail y fintech." />
</svelte:head>

<main>
    <Navbar socials={data.socials}/>
    <Presentation about={data.about} socials={data.socials} profession={data.profession}/>
    <Jobs jobs={data.jobs} techs={data.techs} />
    <Skills skills={data.skills} techs={data.techs} />
    <Podcast podcasts={data.podcasts} techs={data.techs}/>
    <Footer socials={data.socials}/>
</main>