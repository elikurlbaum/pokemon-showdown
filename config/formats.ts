// Note: This is the list of formats
// The rules that formats use are stored in data/rulesets.ts
/*
If you want to add custom formats, create a file in this folder named: "custom-formats.ts"

Paste the following code into the file and add your desired formats and their sections between the brackets:
--------------------------------------------------------------------------------
// Note: This is the list of formats
// The rules that formats use are stored in data/rulesets.ts

export const Formats: FormatList = [
];
--------------------------------------------------------------------------------

If you specify a section that already exists, your format will be added to the bottom of that section.
New sections will be added to the bottom of the specified column.
The column value will be ignored for repeat sections.
*/

export const Formats: import("../sim/dex-formats").FormatList = [
	// Pokemon Draft League
	///////////////////////////////////////////////////////////////////

	{
		section: "Pokemon Draft League",
	},
	{
		name: "[Gen 9] PDL Season 2",
		mod: "gen9",
		gameType: "doubles",
		effectType: "Format",
		desc: "PDL Season 2!",
		ruleset: [
			"Flat Rules",
			"+past",
			"+future",
			"!! Adjust Level = 50",
			"One Mega or Tera Clause",
		],
		banlist: [],
		unbanlist: [],
		challengeShow: true,
		searchShow: true,
		tournamentShow: true,
		bestOfDefault: true,
	},
	{
		name: "[Gen 9] PDL Season 1",
		mod: "gen9",
		gameType: "doubles",
		effectType: "Format",
		desc: "PDL Season 1!",
		ruleset: [
			"Flat Rules",
			"+past",
			"!! Adjust Level = 50",
			"One Mega or Tera Clause",
		],
		banlist: [],
		challengeShow: true,
		searchShow: true,
		tournamentShow: true,
		bestOfDefault: true,
	},
];
