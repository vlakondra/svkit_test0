<!-- <script context="module">
const nodecallspython = require("node-calls-python");

const py = nodecallspython.interpreter;


</script> -->
<script>
	import Inputd from './inputd.svelte';

	//  import  * as api  from 'node-calls-python';
	//  const py = api.interpreter;

	
	
	 // py.import('test.py',false).then(async function (pymodule) {
	// 	const result = await py.call(pymodule, 'multiple', [1, 2, 3, 4], [2, 3, 4, 5]);
	// 	console.log(result);
	// });

	function myEventHandler(e) {
		console.log('--??--', e.detail.myName);

		try {
			e.detail.myName.focus();
			e.detail.myName.showPicker();
		} catch (err) {
			console.log(err);
		}
	}
</script>

<p>
	<button >Show Picker</button>
</p>

<div>
	<a href='/blog'>blog</a>
</div>
<div  style="padding:20px;background:silver">
	<p>
		<Inputd on:myEvent={myEventHandler} />

		<!-- <input id='dtp' class="datepicker1" on:mousemove={func} bind:this={inputEl} type='datetime-local' /> -->
	</p>
</div>

<p>
	<a href=" https://github.com/gitpod-samples/template-sveltekit/tree/main">Template </a>
</p>

<style>
	.datepicker {
		position: relative;
		cursor: pointer;
		box-sizing: border-box;
		line-height: normal !important;
	}
	.datepicker::-webkit-calendar-picker-indicator {
		position: absolute;
		right: 0;
		width: 100%;
		height: 100%;
		margin: 0;
		padding: 0;
		opacity: 0;
		cursor: pointer;
	}
</style>
