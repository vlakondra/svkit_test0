<script>
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();


	function func(ev) {
		dispatch('myEvent', {
			r:ev.currentTarget.click(),
			myName: ev.currentTarget
		});
	}
</script>

<div>
	<input on:mousemove={func}  type="datetime-local" />
</div>
