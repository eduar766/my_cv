<script>
    import Navbar from '../components/Navbar.svelte';
    import Presentation from '../components/Presentation.svelte';
    import Jobs from '../components/Jobs.svelte';
    import Skills from '../components/Skills.svelte';
    import Footer from '../components/Footer.svelte';
    import Podcast from '../components/Podcast.svelte';

    import data from'../eduardo.json';
</script>

<svelte:head>
	<title>Eduardo Saavedra</title>
</svelte:head>

<div>
    <Navbar socials={data.socials}/>
    <Presentation about={data.about} socials={data.socials} profession={data.profession}/>
    <Jobs jobs={data.jobs} techs={data.techs} />
    <Skills skills={data.skills} techs={data.techs} />
    <Podcast podcasts={data.podcasts} techs={data.techs}/>
    <Footer socials={data.socials}/>
</div>