<script>
    import Navbar from '../components/Navbar.svelte';
    import Presentation from '../components/Presentation.svelte';
    import Jobs from '../components/Jobs.svelte'

    import data from'../eduardo.json';
</script>

<svelte:head>
	<title>Eduardo Saavedra</title>
</svelte:head>

<div>
    <Navbar socials={data.socials}/>
    <Presentation about={data.about} socials={data.socials}/>
    <Jobs jobs={data.jobs}/>
</div>