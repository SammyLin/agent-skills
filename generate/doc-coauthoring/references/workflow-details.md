# Doc Co-Authoring: Detailed Workflow Reference

## Stage 1: Context Gathering (Detailed)

### Initial Questions

Start by asking for meta-context:
1. What type of document? (technical spec, decision doc, proposal)
2. Who's the primary audience?
3. What's the desired impact when someone reads this?
4. Is there a template or format to follow?
5. Any other constraints or context?

Inform them they can answer in shorthand or dump information however works best.

**If user provides a template or mentions a doc type:**
- Ask if they have a template document to share
- If they provide a link, use appropriate integration to fetch it
- If they provide a file, read it

**If user mentions editing an existing shared document:**
- Read the current state
- Check for images without alt-text
- If images exist without alt-text, explain Claude won't see them and offer alt-text generation

### Info Dumping

Encourage dumping all context:
- Background on the project/problem
- Related team discussions or shared documents
- Why alternative solutions aren't being used
- Organizational context (team dynamics, past incidents, politics)
- Timeline pressures or constraints
- Technical architecture or dependencies
- Stakeholder concerns

Offer multiple ways: stream-of-consciousness, point to channels/threads, link to shared docs.

**If integrations available**: Mention they can pull context from messaging apps and document storage directly.

**If no integrations**: Suggest enabling connectors in Claude settings, or paste content directly.

**During context gathering:**
- If user mentions channels/docs: use integrations if available, otherwise ask for paste
- If user mentions unknown entities: ask if connected tools should be searched (wait for confirmation)
- Track what's learned and what's unclear

**Asking clarifying questions:**
- Generate 5-10 numbered questions based on gaps
- Let them use shorthand (e.g., "1: yes, 2: see #channel, 3: no because backwards compat")

**Exit condition:** Questions show understanding - can ask about edge cases and trade-offs without needing basics explained.

## Stage 2: Refinement & Structure (Detailed)

### Section Ordering

If structure is clear: Ask which section to start with. Suggest starting with most unknowns.
If user doesn't know sections: Suggest 3-5 sections appropriate for the doc type.

### Create Initial Structure

**If artifacts available:** Use `create_file` to create artifact with section headers and "[To be written]" placeholders.
**If no artifacts:** Create markdown file (e.g., `decision-doc.md`, `technical-spec.md`).

### For Each Section

#### Step 1: Clarifying Questions
Announce the section. Ask 5-10 specific questions about what should be included.

#### Step 2: Brainstorming
Brainstorm 5-20 items depending on complexity. Look for:
- Context shared that might have been forgotten
- Angles or considerations not yet mentioned
Offer to brainstorm more.

#### Step 3: Curation
Ask which points to keep/remove/combine with brief justifications. Examples:
- "Keep 1,4,7,9"
- "Remove 3 (duplicates 1)"
- "Combine 11 and 12"

If user gives freeform feedback, extract preferences and proceed.

#### Step 4: Gap Check
Ask if anything important is missing for the section.

#### Step 5: Drafting
Use `str_replace` to replace placeholder with drafted content. After drafting, provide link/confirm.

**Key instruction (first section):** Ask user to indicate changes rather than editing directly, to help learn their style.

#### Step 6: Iterative Refinement
- Use `str_replace` for edits (never reprint whole doc)
- If user edits directly, note their changes for future sections
- Continue until satisfied

### Quality Checking
After 3 consecutive iterations with no substantial changes, ask if anything can be removed.

### Near Completion
At 80%+ sections done:
- Re-read entire document
- Check flow, consistency, redundancy, contradictions
- Check for "slop" or generic filler
- Ensure every sentence carries weight

## Stage 3: Reader Testing (Detailed)

### With Sub-Agents (e.g., Claude Code)

1. **Predict 5-10 reader questions** readers would realistically ask
2. **Test with sub-agent** - invoke with just document + question, no conversation context
3. **Run additional checks** - ambiguity, false assumptions, contradictions
4. **Report and fix** - loop back to refinement for problematic sections

### Without Sub-Agents (e.g., claude.ai)

1. **Predict 5-10 reader questions**
2. **Setup testing**:
   - Open fresh Claude conversation
   - Paste/share document
   - Ask Reader Claude each question
   - For each: get answer, ambiguity notes, assumed knowledge
3. **Additional checks**: Ask Reader Claude about ambiguity, assumed knowledge, contradictions
4. **Iterate** based on what Reader Claude got wrong

### Exit Condition
Reader Claude consistently answers correctly and doesn't surface new gaps.

## Final Review

1. Recommend final read-through - they own quality
2. Suggest double-checking facts, links, technical details
3. Verify it achieves desired impact

**Final tips:**
- Consider linking conversation in appendix
- Use appendices for depth without bloating main doc
- Update as feedback comes from real readers

## Tips for Effective Guidance

**Tone:** Direct and procedural. Brief rationale when it affects behavior. Don't "sell" the approach.

**Handling Deviations:**
- Skip request: Ask if they want freeform instead
- Frustration: Acknowledge, suggest faster paths
- Always give agency to adjust

**Context Management:** Proactively ask about gaps. Don't let them accumulate.

**Artifact Management:**
- `create_file` for full sections
- `str_replace` for all edits
- Link after every change
- Never use artifacts for brainstorming lists

**Quality over Speed:** Don't rush. Each iteration should make meaningful improvements. Goal: a document that works for readers.
