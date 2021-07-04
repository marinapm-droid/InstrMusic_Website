s.boot;
(
s.plotTree;
s.meter;
~listaUtilizadores = List.new();
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////GO GO GO GO//////
OSCdef.freeAll;
OSCdef.new(\comecar, {
	arg msg;
	msg[0].postln;

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC IP//////

OSCdef.new(\ip, {
	arg msg;
	~ip = msg[1];
	~ip.postln;
	~listaUtilizadores.add(~ip.asString);
	~listaUtilizadores.postln;

	//Enviar mensagem OSC dos efeitos.
	b = NetAddr.new(~ip.asString, 5679);    // create the NetAddr
	b.sendMsg('/effect', "Volume", "Delay", "Vibrato", "Phaser", "Distortion", "Flanger", "Bass", "Pitch", "Reverb", "Tremolo", "Rate");


	//Enviar mensagem OSC dos sons.
	~lista = List["OneMoreTime", "Violino", "Violoncelo", "Chuva", "Guitarra", "Piano", "Ave", "Não"];
	~myPath = PathName.new("D:/Aulas/Faculdade/supercollider/sons");

	~for = ~myPath.entries.collect{
		arg item;
			if (item.fileName.contains(~ip.asString),{
			~lista = ~lista.add(item.fileName.replace(".wav", ""));
		});
	};
	a = NetAddr.new(~ip.asString, 5650);    // create the NetAddr
	a.sendMsg('/sound', ~lista.asString);

},"/ip");
//////////////////////////////////////////////////////////////////////////////////////////////////////////////CRIAÇÃO DE VARIÁVEIS//////

~sensor = "sensor";
~sound = "sound";
~conta = 0;
~count = 0;
//r = Recorder(s);
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC EFFECT_GERAL//////


OSCdef.new("\home", {
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////FOR LISTA_USER//////
	~listaUtilizadores.do({ arg item, i;
			var sound;
			var group = Group.new;
			var volume, delay, tremolo, distortion, pitch, reverb;


			OSCdef.new("\removeUser".catArgs(item.asString), {
				msg[1].postln;
				OSCdef(\sound ++ item.asSymbol).free;
				OSCdef(\sensorAccelerometer ++ item.asSymbol).free;
				group.free;
			},"/exit".catArgs(item.asString));
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC SOUND//////
			OSCdef.new("\sound".catArgs(item.asString), {
				arg msg;
				case
				{msg[1] == 'OneMoreTime'} {sound = Buffer.read(s, "D:/Aulas/Faculdade/supercollider/sons/one.wav")}
				{msg[1] == 'Violino'} {sound = Buffer.read(s, "D:/Aulas/Faculdade/supercollider/sons/violino.wav")}
				{msg[1] == 'Violoncelo'} {sound = Buffer.read(s, "D:/Aulas/Faculdade/supercollider/sons/violoncelo.wav")}
				{msg[1] == 'Não'} {sound = Buffer.read(s, "D:/Aulas/Faculdade/supercollider/sons/não.wav")};
				Routine{s.sync; 0.1.wait; group.set(\buf, sound, \trig, 1); 0.1.wait; group.set(\trig, 0);}.play;
				msg[1].postln;
				},"/sound".catArgs(item.asString));

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC EFFECT_USER//////

			OSCdef.new("\effect".catArgs(item.asString), {
				arg msg;
				var effect = msg[1];
				msg[1].postln;

////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC ACCELEROMETER//////

				OSCdef.new("\sensorAccelerometer".catArgs(item.asString), {
					arg msg;
					case
					{effect == 'Volume'} {
						volume.set(\amp, msg[1].linlin(-3, 11, 0, 1));
						msg[1].linlin(-3, 11, 0, 1).postln;
					}
					{effect == 'Delay'} {
						delay.set(\delTime, msg[1]);
						delay.set(\decayTime, msg[2]);
					}
					{effect == 'Tremolo'} {
						tremolo.set(\freq, msg[1].linlin(-3,11,0.1,15));
						//msg[1].linlin(-3,11,0,15).postln;
					}
					{effect == "Phaser"} {}
					{effect == 'Distortion'} {
						distortion.set(\pregain, msg[1].linlin(-3,11,0.1,15));
						msg[1].linlin(-3,11,0,15).postln;
					}
					{effect == "Flanger"} {}
					{effect == "Bass"} {}
					{effect == 'Rate'} {
						volume.set(\rate, msg[1].linexp(-3, 11, 0.25, 4));
						msg[1].linexp(-3, 11, 0.25, 4).postln;
					}
					{effect == 'Pitch'} {
						volume.set(\rate, msg[1].linexp(-3, 11, 0.25, 4));
						msg[1].linexp(-3, 11, 0.25, 4).postln;
					}

					{true} {};
				},"/accelerometer".catArgs(item.asString));

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC TOUCH1//////

				OSCdef.new("\sensorTouch1".catArgs(item.asString), {
					arg msg;

					case
					{effect == 'Volume'} {volume.set(\amp, msg[1]);}
					{effect == 'Delay'} {delay.set(\delTime, msg[1].linlin(0,1,0,4));
						msg[1].linlin(0,1,0,4).postln;
						msg[2].linlin(0,1,0,4).postln;
						delay.set(\decayTime, msg[2].linlin(0,1,0,4));
					}
					{effect == 'Tremolo'} {
						tremolo.set(\freq, msg[1].linlin(0,1,0.1,15));
						msg[1].linlin(0,1,0,15).postln;
					}
					{effect == "Phaser"} {}
					{effect == 'Distortion'} {
						distortion.set(\pregain, msg[1].linlin(0,1,0.1,15));
						msg[1].linlin(0,1,0,15).postln;

					}
					{effect == "Flanger"} {}
					{effect == "Bass"} {}
					{effect == "Pitch"} {}
					{effect == 'Reverb'} {
						reverb.set(\room, msg[1]);
						msg[1].postln;
					}
					{effect == 'Pitch'} {
						if (msg[1] < 0.50046253204346) {
							pitch.set(\pitch1, msg[1].linexp(0, 1, 0.5, 1));
							pitch.set(\pitch2, msg[1].linexp(0, 1, 0.5, 1));
							msg[1].linexp(0, 1, 0, 0.4).postln;
						} {
							pitch.set(\pitch1, msg[1].linexp(0, 1, 1, 1.5));
							pitch.set(\pitch2, msg[1].linexp(0, 1, 1, 1.5));
							msg[1].postln;
						}
					}
					{true} {};
				},"/touch1".catArgs(item.asString));

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC PLAY MUSIC//////

				OSCdef.new("\play".catArgs(item.asString), {
					arg msg;
					if(~count == 1, {
						group.set(\rate, 1, \buf, sound);
						msg[0].postln;
					},{
						msg[0].postln;
						case
						{effect == 'Volume'} {volume = Synth.new(\volume, [\buf, sound], target: group);}
						{effect == 'Delay'} {delay = Synth.new(\delay1, [\buf, sound], target: group);}
						{effect == 'Tremolo'} {tremolo = Synth.new(\tremolo, [\buf, sound], target: group);}
						{effect == 'Phaser'} {}
						{effect == 'Distortion'} {distortion = Synth.new(\distortion, [\buf, sound], target: group);}
						{effect == 'Flanger'} {}
						{effect == 'Bass'} {}
						{effect == 'Pitch'} {pitch = Synth.new(\octave, [\buf, sound], target: group);}
						{effect == 'Reverb'} {reverb = Synth.new(\reverb, [\buf, sound], target: group);}
						{true} {}
					})
				}, "/play".catArgs(item.asString));

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC PAUSE MUSIC//////

				OSCdef.new("\pause".catArgs(item.asString), {
					arg msg;
					~count = 1;
					msg[0].postln;
					group.set(\rate, 0);
				}, "/pause".catArgs(item.asString));

				/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC STOP//////

				OSCdef.new("\stop".catArgs(item.asString), {
					~count = 0;
					group.freeAll;
				}, "/stop".catArgs(item.asString));

			},"/effect".catArgs(item.asString));  //FECHAR FUNC EFFECT DO UTILIZADOR

			/////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC START_RECORD//////

			OSCdef.new("\record".catArgs(item.asString), {
				arg msg;
				var msg1 = msg[1].asString;
				//r.filePrefix = msg1;
				//~lista.add(msg1.catArgs(~conta));
				//s.prepareForRecord("D:\\Aulas\\Faculdade\\supercollider\\sons\\" ++ item.asString ++ ".wav");
				s.recHeaderFormat = "wav";
				s.record;
				//~conta = ~conta + 1;
				msg[0].postln;
			}, "/startRecord".catArgs(item.asString));

			//////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC STOP_RECORD//////

			OSCdef.new("\stopRecord".catArgs(item.asString), {
				arg msg;
				msg[0].postln;
				msg[1].postln;
				r.stopRecording;
			}, "/stopRecord".catArgs(item.asString));
/////////////////////////////////////////////////////////////////////////////////////////////////////////FECHAR FOR CICLE DA LISTA//////

		});

///////////////////////////////////////////////////////////////////////////////////////////////////////////FECHAR FUN EFFECT GERAL//////

	},"/home");

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC VOLUME//////

SynthDef.new(\volume, {
	arg amp=1, buf = 0, rate = 1, spos=0, pan=1, out=0, trig = 0;
	var sig;
	sig = PlayBuf.ar(2, buf, BufRateScale.kr(buf)*rate, doneAction: 0, loop: 1, trigger: trig);
	sig = Pan2.ar(sig,pan,amp.lag(0.1));
	Out.ar(out,sig);
}).add;


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC DELAY//////

SynthDef(\delay1,{
	arg buf = 0, maxDel = 4, delTime=1, decayTime = 1;
	Out.ar(0, AllpassL.ar(PlayBuf.ar(2, buf, doneAction: 0, loop: 0, trigger: 1), maxDel, delTime.lag(0.1), decayTime))
}).add;


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC DISTORTION//////

SynthDef(\distortion, {
		arg buf=0, outbus=0, pregain=0.001, postgain=1, mix = 0.5, level=0, rate = 1;
		var sig, sigtocomp, fx, y, z;
	    sig = PlayBuf.ar(2, buf, BufRateScale.kr(buf)*rate, doneAction: 0, loop: 1, trigger: 1);
		sigtocomp = ((sig * pregain).distort * postgain).distort;
		fx = Compander.ar(sigtocomp, sigtocomp, 1, 0, 1 );
		Out.ar(outbus, LeakDC.ar((fx * mix) + (sig * level)));
}).add;

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC REVERB//////

SynthDef(\reverb, {
	    arg inbus=0, outbus=0, mix=0.70, room=0, damp=1, fxlevel=0.75, level=0, buf=0, rate=1;
		var fx, sig;
		sig = PlayBuf.ar(2, buf, BufRateScale.kr(buf)*rate, doneAction: 0, loop: 1, trigger: 1);
		fx = FreeVerb.ar(sig, mix, room, damp);
		Out.ar(outbus, (fx*fxlevel) + (sig * level));

		}).add;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC TREMOLO//////

SynthDef(\tremolo, {
	    arg inbus=0, outbus=0, freq=1, strength=1, fxlevel=0.5, level=0, buf=0, rate=1, trig = 0;
		var fx, sig;
		sig = PlayBuf.ar(2, buf, BufRateScale.kr(buf)*rate, doneAction: 0, loop: 1, trigger: trig);
		fx = sig * SinOsc.ar(freq, 0, strength, 1);
		Out.ar(outbus, (fxlevel * fx) + (sig * level));
		}).add;

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC OCTAVE//////


SynthDef(\octave, {
		arg inbus=0, outbus=0, pitch1=1, pitch2=1, vol1=0.25, vol2=0.25, dispersion=0, fxlevel=0.5, level=0, buf=0, rate=1;
		var fx1, fx2, sig;
		sig = PlayBuf.ar(2, buf, BufRateScale.kr(buf)*rate, doneAction: 0, loop: 1, trigger: 1);
		fx1 = PitchShift.ar(sig, 0.2, pitch1, dispersion, 0.0001);
		fx2 = PitchShift.ar(sig, 0.2, pitch2, dispersion, 0.0001);
		Out.ar(outbus,  ( ((fx1 * vol1) + (fx2 * vol2)) * fxlevel) + (sig * level) );
}).add;

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC GYROSCOPE//////


OSCdef.new(\sensorGyroscope, {
	arg msg;
	(
	case
		{~effect == "Volume"} {}
		{~effect == "Delay"} {}
		{~effect == "Tremolo"} {}
		{~effect == "Phaser"} {}
		{~effect == "Distortion"} {}
		{~effect == "Flanger"} {}
		{~effect == "Bass"} {}
		{~effect == "Pitch"} {}
		{true} {}
	)
},"/gyroscope");

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////FUNC TOUCH2//////

OSCdef.new(\sensorTouch2, {
	arg msg;
	(
	case
		{~effect == "Volume"} {}
		{~effect == "Delay"} {}
		{~effect == "Tremolo"} {}
		{~effect == "Phaser"} {}
		{~effect == "Distortion"} {}
		{~effect == "Flanger"} {}
		{~effect == "Bass"} {}
		{~effect == "Pitch"} {}
		{true} {}
	)
},"/touch2");

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////GO GO GO GO//////

}, "/GO");
)