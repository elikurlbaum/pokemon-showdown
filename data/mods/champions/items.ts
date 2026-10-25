export const Items: import('../../../sim/dex-items').ModdedItemDataTable = {
	abilityshield: {
		inherit: true,
		isNonstandard: null,
	},
	abomasite: {
		inherit: true,
		isNonstandard: null,
	},
	absolite: {
		inherit: true,
		isNonstandard: null,
	},
	absolitez: {
		inherit: true,
		isNonstandard: null,
	},
	absorbbulb: {
		inherit: true,
		isNonstandard: null,
	},
	adamantcrystal: {
		inherit: true,
		isNonstandard: null,
	},
	adamantorb: {
		inherit: true,
		isNonstandard: null,
	},
	adrenalineorb: {
		inherit: true,
		isNonstandard: null,
	},
	aerodactylite: {
		inherit: true,
		isNonstandard: null,
	},
	aggronite: {
		inherit: true,
		isNonstandard: null,
	},
	aguavberry: {
		inherit: true,
		isNonstandard: null,
	},
	alakazite: {
		inherit: true,
		isNonstandard: null,
	},
	altarianite: {
		inherit: true,
		isNonstandard: null,
	},
	ampharosite: {
		inherit: true,
		isNonstandard: null,
	},
	apicotberry: {
		inherit: true,
		isNonstandard: null,
	},
	assaultvest: {
		inherit: true,
		isNonstandard: null,
	},
	audinite: {
		inherit: true,
		isNonstandard: null,
	},
	auspiciousarmor: {
		inherit: true,
		isNonstandard: null,
	},
	banettite: {
		inherit: true,
		isNonstandard: null,
	},
	barbaracite: {
		inherit: true,
		isNonstandard: null,
	},
	baxcalibrite: {
		inherit: true,
		isNonstandard: null,
	},
	beastball: {
		inherit: true,
		isNonstandard: null,
	},
	beedrillite: {
		inherit: true,
		isNonstandard: null,
	},
	berrysweet: {
		inherit: true,
		isNonstandard: null,
	},
	bignugget: {
		inherit: true,
		isNonstandard: null,
	},
	blacksludge: {
		inherit: true,
		isNonstandard: null,
	},
	blastoisinite: {
		inherit: true,
		isNonstandard: null,
	},
	blazikenite: {
		inherit: true,
		isNonstandard: null,
	},
	blunderpolicy: {
		inherit: true,
		isNonstandard: null,
	},
	boosterenergy: {
		inherit: true,
		isNonstandard: null,
	},
	bottlecap: {
		inherit: true,
		isNonstandard: null,
	},
	cameruptite: {
		inherit: true,
		isNonstandard: null,
	},
	cellbattery: {
		inherit: true,
		isNonstandard: null,
	},
	chandelurite: {
		inherit: true,
		isNonstandard: null,
	},
	charizarditex: {
		inherit: true,
		isNonstandard: null,
	},
	charizarditey: {
		inherit: true,
		isNonstandard: null,
	},
	chesnaughtite: {
		inherit: true,
		isNonstandard: null,
	},
	chimechite: {
		inherit: true,
		isNonstandard: null,
	},
	chippedpot: {
		inherit: true,
		isNonstandard: null,
	},
	choiceband: {
		inherit: true,
		isNonstandard: null,
	},
	choicespecs: {
		inherit: true,
		isNonstandard: null,
	},
	clearamulet: {
		inherit: true,
		isNonstandard: null,
	},
	clefablite: {
		inherit: true,
		isNonstandard: null,
	},
	cloversweet: {
		inherit: true,
		isNonstandard: null,
	},
	cornerstonemask: {
		inherit: true,
		isNonstandard: null,
	},
	covertcloak: {
		inherit: true,
		isNonstandard: null,
	},
	crabominite: {
		inherit: true,
		isNonstandard: null,
	},
	crackedpot: {
		inherit: true,
		isNonstandard: null,
	},
	custapberry: {
		inherit: true,
		isNonstandard: null,
	},
	dawnstone: {
		inherit: true,
		isNonstandard: null,
	},
	delphoxite: {
		inherit: true,
		isNonstandard: null,
	},
	destinyknot: {
		inherit: true,
		isNonstandard: null,
	},
	diveball: {
		inherit: true,
		isNonstandard: null,
	},
	dracoplate: {
		inherit: true,
		isNonstandard: null,
	},
	dragalgite: {
		inherit: true,
		isNonstandard: null,
	},
	dragoninite: {
		inherit: true,
		isNonstandard: null,
	},
	dragonscale: {
		inherit: true,
		isNonstandard: null,
	},
	drampanite: {
		inherit: true,
		isNonstandard: null,
	},
	dreadplate: {
		inherit: true,
		isNonstandard: null,
	},
	dreamball: {
		inherit: true,
		isNonstandard: null,
	},
	dubiousdisc: {
		inherit: true,
		isNonstandard: null,
	},
	duskball: {
		inherit: true,
		isNonstandard: null,
	},
	duskstone: {
		inherit: true,
		isNonstandard: null,
	},
	earthplate: {
		inherit: true,
		isNonstandard: null,
	},
	eelektrossite: {
		inherit: true,
		isNonstandard: null,
	},
	ejectbutton: {
		inherit: true,
		onAfterMoveSecondary(target, source, move) {
			if (source && source !== target && target.hp && move && move.category !== 'Status' && !move.flags['futuremove']) {
				if (!this.canSwitch(target.side) || target.forceSwitchFlag || target.beingCalledBack || target.isSkyDropped()) return;
				if (target.volatiles['commanding'] || target.volatiles['commanded']) return;
				for (const pokemon of this.getAllActive()) {
					if (pokemon.switchFlag === true) return;
				}
				target.switchFlag = true;
				if (!target.useItem()) {
					target.switchFlag = false;
				}
			}
		},
	},
	ejectpack: {
		inherit: true,
		isNonstandard: null,
	},
	electirizer: {
		inherit: true,
		isNonstandard: null,
	},
	emboarite: {
		inherit: true,
		isNonstandard: null,
	},
	enigmaberry: {
		inherit: true,
		isNonstandard: null,
	},
	eviolite: {
		inherit: true,
		isNonstandard: null,
	},
	excadrite: {
		inherit: true,
		isNonstandard: null,
	},
	falinksite: {
		inherit: true,
		isNonstandard: null,
	},
	fastball: {
		inherit: true,
		isNonstandard: null,
	},
	feraligite: {
		inherit: true,
		isNonstandard: null,
	},
	figyberry: {
		inherit: true,
		isNonstandard: null,
	},
	firestone: {
		inherit: true,
		isNonstandard: null,
	},
	fistplate: {
		inherit: true,
		isNonstandard: null,
	},
	flameorb: {
		inherit: true,
		isNonstandard: null,
	},
	flameplate: {
		inherit: true,
		isNonstandard: null,
	},
	floatstone: {
		inherit: true,
		isNonstandard: null,
	},
	floettite: {
		inherit: true,
		isNonstandard: null,
	},
	flowersweet: {
		inherit: true,
		isNonstandard: null,
	},
	friendball: {
		inherit: true,
		isNonstandard: null,
	},
	froslassite: {
		inherit: true,
		isNonstandard: null,
	},
	galaricacuff: {
		inherit: true,
		isNonstandard: null,
	},
	galaricawreath: {
		inherit: true,
		isNonstandard: null,
	},
	galladite: {
		inherit: true,
		isNonstandard: null,
	},
	ganlonberry: {
		inherit: true,
		isNonstandard: null,
	},
	garchompite: {
		inherit: true,
		isNonstandard: null,
	},
	garchompitez: {
		inherit: true,
		isNonstandard: null,
	},
	gardevoirite: {
		inherit: true,
		isNonstandard: null,
	},
	gengarite: {
		inherit: true,
		isNonstandard: null,
	},
	glalitite: {
		inherit: true,
		isNonstandard: null,
	},
	glimmoranite: {
		inherit: true,
		isNonstandard: null,
	},
	goldbottlecap: {
		inherit: true,
		isNonstandard: null,
	},
	golisopite: {
		inherit: true,
		isNonstandard: null,
	},
	golurkite: {
		inherit: true,
		isNonstandard: null,
	},
	greatball: {
		inherit: true,
		isNonstandard: null,
	},
	greninjite: {
		inherit: true,
		isNonstandard: null,
	},
	grepaberry: {
		inherit: true,
		isNonstandard: null,
	},
	gripclaw: {
		inherit: true,
		isNonstandard: null,
	},
	griseouscore: {
		inherit: true,
		isNonstandard: null,
	},
	griseousorb: {
		inherit: true,
		isNonstandard: null,
	},
	gyaradosite: {
		inherit: true,
		isNonstandard: null,
	},
	hawluchanite: {
		inherit: true,
		isNonstandard: null,
	},
	healball: {
		inherit: true,
		isNonstandard: null,
	},
	hearthflamemask: {
		inherit: true,
		isNonstandard: null,
	},
	heavyball: {
		inherit: true,
		isNonstandard: null,
	},
	heavydutyboots: {
		inherit: true,
		isNonstandard: null,
	},
	heracronite: {
		inherit: true,
		isNonstandard: null,
	},
	hondewberry: {
		inherit: true,
		isNonstandard: null,
	},
	houndoominite: {
		inherit: true,
		isNonstandard: null,
	},
	iapapaberry: {
		inherit: true,
		isNonstandard: null,
	},
	icestone: {
		inherit: true,
		isNonstandard: null,
	},
	icicleplate: {
		inherit: true,
		isNonstandard: null,
	},
	insectplate: {
		inherit: true,
		isNonstandard: null,
	},
	ironplate: {
		inherit: true,
		isNonstandard: null,
	},
	jabocaberry: {
		inherit: true,
		isNonstandard: null,
	},
	kangaskhanite: {
		inherit: true,
		isNonstandard: null,
	},
	keeberry: {
		inherit: true,
		isNonstandard: null,
	},
	kelpsyberry: {
		inherit: true,
		isNonstandard: null,
	},
	laggingtail: {
		inherit: true,
		isNonstandard: null,
	},
	lansatberry: {
		inherit: true,
		isNonstandard: null,
	},
	leafstone: {
		inherit: true,
		isNonstandard: null,
	},
	leek: {
		inherit: true,
		isNonstandard: null,
	},
	levelball: {
		inherit: true,
		isNonstandard: null,
	},
	liechiberry: {
		inherit: true,
		isNonstandard: null,
	},
	loadeddice: {
		inherit: true,
		isNonstandard: null,
	},
	lopunnite: {
		inherit: true,
		isNonstandard: null,
	},
	loveball: {
		inherit: true,
		isNonstandard: null,
	},
	lovesweet: {
		inherit: true,
		isNonstandard: null,
	},
	lucarionite: {
		inherit: true,
		isNonstandard: null,
	},
	lucarionitez: {
		inherit: true,
		isNonstandard: null,
	},
	luminousmoss: {
		inherit: true,
		isNonstandard: null,
	},
	lureball: {
		inherit: true,
		isNonstandard: null,
	},
	lustrousglobe: {
		inherit: true,
		isNonstandard: null,
	},
	lustrousorb: {
		inherit: true,
		isNonstandard: null,
	},
	luxuryball: {
		inherit: true,
		isNonstandard: null,
	},
	magmarizer: {
		inherit: true,
		isNonstandard: null,
	},
	magoberry: {
		inherit: true,
		isNonstandard: null,
	},
	malamarite: {
		inherit: true,
		isNonstandard: null,
	},
	maliciousarmor: {
		inherit: true,
		isNonstandard: null,
	},
	manectite: {
		inherit: true,
		isNonstandard: null,
	},
	marangaberry: {
		inherit: true,
		isNonstandard: null,
	},
	masterball: {
		inherit: true,
		isNonstandard: null,
	},
	masterpieceteacup: {
		inherit: true,
		isNonstandard: null,
	},
	mawilite: {
		inherit: true,
		isNonstandard: null,
	},
	meadowplate: {
		inherit: true,
		isNonstandard: null,
	},
	medichamite: {
		inherit: true,
		isNonstandard: null,
	},
	meganiumite: {
		inherit: true,
		isNonstandard: null,
	},
	meowsticite: {
		inherit: true,
		isNonstandard: null,
	},
	metalalloy: {
		inherit: true,
		isNonstandard: null,
	},
	metagrossite: {
		inherit: true,
		isNonstandard: null,
	},
	micleberry: {
		inherit: true,
		isNonstandard: null,
	},
	mindplate: {
		inherit: true,
		isNonstandard: null,
	},
	mirrorherb: {
		inherit: true,
		isNonstandard: null,
	},
	moonball: {
		inherit: true,
		isNonstandard: null,
	},
	moonstone: {
		inherit: true,
		isNonstandard: null,
	},
	nestball: {
		inherit: true,
		isNonstandard: null,
	},
	netball: {
		inherit: true,
		isNonstandard: null,
	},
	ovalstone: {
		inherit: true,
		isNonstandard: null,
	},
	parkball: {
		inherit: true,
		isNonstandard: null,
	},
	petayaberry: {
		inherit: true,
		isNonstandard: null,
	},
	pidgeotite: {
		inherit: true,
		isNonstandard: null,
	},
	pinsirite: {
		inherit: true,
		isNonstandard: null,
	},
	pixieplate: {
		inherit: true,
		isNonstandard: null,
	},
	pokeball: {
		inherit: true,
		isNonstandard: null,
	},
	pomegberry: {
		inherit: true,
		isNonstandard: null,
	},
	poweranklet: {
		inherit: true,
		isNonstandard: null,
	},
	powerband: {
		inherit: true,
		isNonstandard: null,
	},
	powerbelt: {
		inherit: true,
		isNonstandard: null,
	},
	powerbracer: {
		inherit: true,
		isNonstandard: null,
	},
	powerherb: {
		inherit: true,
		isNonstandard: null,
	},
	powerlens: {
		inherit: true,
		isNonstandard: null,
	},
	powerweight: {
		inherit: true,
		isNonstandard: null,
	},
	premierball: {
		inherit: true,
		isNonstandard: null,
	},
	prettyfeather: {
		inherit: true,
		isNonstandard: null,
	},
	prismscale: {
		inherit: true,
		isNonstandard: null,
	},
	protectivepads: {
		inherit: true,
		isNonstandard: null,
	},
	protector: {
		inherit: true,
		isNonstandard: null,
	},
	punchingglove: {
		inherit: true,
		isNonstandard: null,
	},
	pyroarite: {
		inherit: true,
		isNonstandard: null,
	},
	qualotberry: {
		inherit: true,
		isNonstandard: null,
	},
	quickball: {
		inherit: true,
		isNonstandard: null,
	},
	raichunitex: {
		inherit: true,
		isNonstandard: null,
	},
	raichunitey: {
		inherit: true,
		isNonstandard: null,
	},
	rarebone: {
		inherit: true,
		isNonstandard: null,
	},
	razorclaw: {
		inherit: true,
		isNonstandard: null,
	},
	razorfang: {
		inherit: true,
		isNonstandard: null,
	},
	reapercloth: {
		inherit: true,
		isNonstandard: null,
	},
	repeatball: {
		inherit: true,
		isNonstandard: null,
	},
	ribbonsweet: {
		inherit: true,
		isNonstandard: null,
	},
	ringtarget: {
		inherit: true,
		isNonstandard: null,
	},
	roomservice: {
		inherit: true,
		isNonstandard: null,
	},
	rowapberry: {
		inherit: true,
		isNonstandard: null,
	},
	rustedshield: {
		inherit: true,
		isNonstandard: null,
	},
	rustedsword: {
		inherit: true,
		isNonstandard: null,
	},
	sablenite: {
		inherit: true,
		isNonstandard: null,
	},
	safariball: {
		inherit: true,
		isNonstandard: null,
	},
	safetygoggles: {
		inherit: true,
		isNonstandard: null,
	},
	salacberry: {
		inherit: true,
		isNonstandard: null,
	},
	salamencite: {
		inherit: true,
		isNonstandard: null,
	},
	sceptilite: {
		inherit: true,
		isNonstandard: null,
	},
	scizorite: {
		inherit: true,
		isNonstandard: null,
	},
	scolipite: {
		inherit: true,
		isNonstandard: null,
	},
	scovillainite: {
		inherit: true,
		isNonstandard: null,
	},
	scraftinite: {
		inherit: true,
		isNonstandard: null,
	},
	sharpedonite: {
		inherit: true,
		isNonstandard: null,
	},
	shinystone: {
		inherit: true,
		isNonstandard: null,
	},
	skarmorite: {
		inherit: true,
		isNonstandard: null,
	},
	skyplate: {
		inherit: true,
		isNonstandard: null,
	},
	slowbronite: {
		inherit: true,
		isNonstandard: null,
	},
	snowball: {
		inherit: true,
		isNonstandard: null,
	},
	souldew: {
		inherit: true,
		isNonstandard: null,
	},
	spelltag: {
		inherit: true,
		isNonstandard: null,
	},
	splashplate: {
		inherit: true,
		isNonstandard: null,
	},
	spookyplate: {
		inherit: true,
		isNonstandard: null,
	},
	sportball: {
		inherit: true,
		isNonstandard: null,
	},
	staraptite: {
		inherit: true,
		isNonstandard: null,
	},
	starfberry: {
		inherit: true,
		isNonstandard: null,
	},
	starminite: {
		inherit: true,
		isNonstandard: null,
	},
	starsweet: {
		inherit: true,
		isNonstandard: null,
	},
	steelixite: {
		inherit: true,
		isNonstandard: null,
	},
	stickybarb: {
		inherit: true,
		isNonstandard: null,
	},
	stoneplate: {
		inherit: true,
		isNonstandard: null,
	},
	strangeball: {
		inherit: true,
		isNonstandard: null,
	},
	strawberrysweet: {
		inherit: true,
		isNonstandard: null,
	},
	sunstone: {
		inherit: true,
		isNonstandard: null,
	},
	sweetapple: {
		inherit: true,
		isNonstandard: null,
	},
	syrupyapple: {
		inherit: true,
		isNonstandard: null,
	},
	swampertite: {
		inherit: true,
		isNonstandard: null,
	},
	tamatoberry: {
		inherit: true,
		isNonstandard: null,
	},
	tartapple: {
		inherit: true,
		isNonstandard: null,
	},
	throatspray: {
		inherit: true,
		isNonstandard: null,
	},
	thunderstone: {
		inherit: true,
		isNonstandard: null,
	},
	timerball: {
		inherit: true,
		isNonstandard: null,
	},
	toxicorb: {
		inherit: true,
		isNonstandard: null,
	},
	toxicplate: {
		inherit: true,
		isNonstandard: null,
	},
	tyranitarite: {
		inherit: true,
		isNonstandard: null,
	},
	ultraball: {
		inherit: true,
		isNonstandard: null,
	},
	unremarkableteacup: {
		inherit: true,
		isNonstandard: null,
	},
	upgrade: {
		inherit: true,
		isNonstandard: null,
	},
	utilityumbrella: {
		inherit: true,
		isNonstandard: null,
	},
	venusaurite: {
		inherit: true,
		isNonstandard: null,
	},
	victreebelite: {
		inherit: true,
		isNonstandard: null,
	},
	waterstone: {
		inherit: true,
		isNonstandard: null,
	},
	weaknesspolicy: {
		inherit: true,
		isNonstandard: null,
	},
	wellspringmask: {
		inherit: true,
		isNonstandard: null,
	},
	wikiberry: {
		inherit: true,
		isNonstandard: null,
	},
	zapplate: {
		inherit: true,
		isNonstandard: null,
	},
};
