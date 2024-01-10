<script>
	export let data;
    console.log(data)
</script>

<h1>BLOG</h1>

{#if data.result}
     <!-- content here -->
    {data.result}
<ul>
	{#each data.result as item}
		<li>{item}</li>
	{/each}
</ul>
{/if}