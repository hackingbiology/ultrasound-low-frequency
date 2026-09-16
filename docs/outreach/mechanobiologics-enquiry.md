# Draft enquiry — Mechanobiologics and UT Health San Antonio

**Status: draft, not sent.** Fabio reviews and sends it from his own address. Two variants below: one for the company, one for the academic group. Keep both short — the full question list lives on the website, and the link does the work.

**Suggested recipients** (to confirm before sending):
- Mechanobiologics, Inc. — via the contact form on mechanobiologics.com; the site lists Linda Kenney as a contact.
- UT Health San Antonio, Barshop Institute — Blake Rasmussen (rasmussenb@uthscsa.edu), principal investigator of NCT07168525; Sanjay Kureel, first author of the Aging Cell paper, now at the Barshop Institute.

---

## Variant A — to Mechanobiologics

**Subject:** Independent open-science replication of the LFU senescence work — a few measurement questions

Dear Dr Kenney,

I am writing on behalf of HackingBiology, a non-profit open-science initiative in Italy. We publish open protocols and biomarker methods for structured self-experimentation at biohack.it, and we have started an open-hardware project to **independently replicate the low-frequency ultrasound work** of Michael Sheetz's group, beginning at the bench with cells rather than with people.

First, condolences on Professor Sheetz's death. The body of work he left is remarkable, and our interest in it is genuine.

Our project is **non-commercial by design**. We sell nothing, ship no hardware, offer no treatments and make no therapeutic claims; we publish documentation, measurements and negative results. We are aware of your patent portfolio — including US 12,714,885 and the pending senescence applications — and we have written a public analysis of what it covers and of the limits we work within.

In trying to reproduce the exposure faithfully, we ran into a set of questions that the papers, the supplementary material and the patent applications do not settle. The most important ones:

1. **Pressure units.** The preprint methods, the Figure S1 axes and the NCT06562374 registration all say "Pa"; the Aging Cell version says "4 kPa". Which is correct?
2. **The measuring instrument.** The Onda MCT-2000 is a cavitation meter reporting a time-averaged total pressure, and its kPa scale requires a self-calibration to an absolute reference. Was that self-calibration performed? Over what averaging interval was the value read? Figure S1B is scaled in millivolts, which suggests the raw probe signal was also used.
3. **Where in the field.** That map shows roughly a ninefold spread across the treatment plane. Does "4 kPa" refer to the centre, the mean, or the peak, and where in the map did the samples sit?
4. **The transducer and drive.** No version of the paper names them. Is the senescence rig the same family as the cancer rig described by Tijore et al. — PZT4 rings with an aluminium cone, epoxy and silicone potted — or a Langevin transducer? Is "135–275 V" peak-to-peak or RMS at the transducer terminals?
5. **Auditory effects.** A whole-body water-coupled exposure at these levels sits above the ACGIH waterborne ceiling, whose evidence base is long-term tinnitus. Were audiograms or tinnitus reports collected in the human pilots?

We would also be glad to know, if you are able to say, why the UTMB osteoarthritis trial was suspended — safety knowledge is the part of this that should be shared regardless of commercial interest.

What we can offer in return: **independent calibration data**. We are building a rig whose acoustic field is mapped and published, with its measurement convention stated in SI units — something nobody outside your group has done. If the effect is real, an independent replication with a documented dose helps you; if our dose turns out not to match yours, better we find out now than after other people start building copies.

The full question list, our evidence review and our IP analysis are public here:
https://hackingbiology.github.io/ultrasound-low-frequency/

I would welcome a conversation, and I am happy to share drafts before we publish anything that concerns your work.

With best regards,

Fabio Pietrosanti
HackingBiology / biohack.it

---

## Variant B — to the Barshop Institute group

**Subject:** Independent replication of the LFU senescence protocol — measurement questions from an open-science group

Dear Professor Rasmussen, dear Dr Kureel,

Congratulations on the XPRIZE Healthspan milestone and on getting the ultrasound spa installed and into a sham-controlled trial. I am writing from HackingBiology, a non-profit open-science initiative in Italy, and we have begun an open-hardware project to replicate the low-frequency ultrasound work at the bench, publishing everything including the failures.

We are stuck on the same thing any replicating group would be stuck on: **the delivered dose is not specified well enough to reproduce.** Our questions are the measurement ones — the units (Pa vs kPa across the preprint, the figures, the paper and the trial registration), what the Onda MCT-2000 reading actually represents, where in a ninefold-varying field the quoted value sits, and which transducer and drive were used, since no version of the paper names them.

Two observations you may find useful, offered in good faith rather than as criticism:

- At 33 kHz a 4 L beaker is a modal cavity, not a beam path — which raises the question of whether the sharp 32.2 kHz optimum is a property of the cells or a mode of that particular vessel. Has the optimum been checked in a different vessel?
- The AJP-Endo diabetes study is largely negative on function and glycaemia, which sits oddly beside the strong performance effects in the lifespan study. How do you read that?

We would also be glad to align our measurement endpoints with yours, so that anything we produce is comparable with NCT07168525 rather than being a parallel island of data.

Our evidence review, open questions and hardware analysis are here:
https://hackingbiology.github.io/ultrasound-low-frequency/

We are not commercial, we sell nothing and we make no health claims; the project exists because independent replication of this result would be valuable whichever way it comes out.

With best regards,

Fabio Pietrosanti
HackingBiology / biohack.it

---

## Notes before sending

- Send from a personal address, not a generic one; a real name gets a reply, an info@ address does not.
- Send the two variants separately, not as a joint email with everyone in copy.
- Do not ask for hardware, files or anything that looks like a request to license or acquire technology — this is a request for measurement clarifications.
- Log any reply in `docs/research/` and update the corresponding question IDs on the open-questions page with the date and source.
- If either party declines or does not answer, that is a fine outcome: it is recorded on the site as an unanswered question, and the project continues as an independent replication.
