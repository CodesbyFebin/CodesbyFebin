# Grok Reference Documentation

**Source**: Extracted from Grok Build workspace  
**Status**: Reference material for systems engineering patterns  
**Last Updated**: October 3, 2026  

---

## Skills Documentation (18 guides)

Comprehensive reference material for building applications with Grok Build TanStack Start framework:

### Authentication & Access
- [Authentication Systems (auth)](skills/auth/SKILL.md) - OAuth, email/password, federated identity, session management
- [Per-User Data & Privacy](skills/auth/references/per-user-data.md) - Multi-tenant architecture patterns

### Database & Storage
- [Neon PostgreSQL (neon)](skills/neon/SKILL.md) - Serverless database integration, connection pooling

### Realtime & Networking
- [Multiplayer P2P (multiplayer-p2p)](skills/multiplayer-p2p/SKILL.md) - WebRTC data channels, mesh networking, synchronization

### Graphics & Game Development
- [Three.js (threejs)](skills/threejs/SKILL.md) - 3D graphics, WebGL, shaders, scene management
- [Building Games (building-games)](skills/building-games/SKILL.md) - Game architecture, frame loops, physics
- [Game Animation Frames](skills/game-animation-frames/SKILL.md) - Motion cycles, sprite sheets, keyframe timing
- [Game Tilesets](skills/game-tilesets/SKILL.md) - Seamless textures, autotiles, terrain transitions
- [Game Characters](skills/game-character-consistency/SKILL.md) - Turnarounds, state variants, equipment changes
- [Game UI & Icons](skills/game-ui-icons/SKILL.md) - Buttons, panels, bars, HUD elements
- [Asset Generation (game-asset-core)](skills/game-asset-core/SKILL.md) - Engine-ready specifications, style anchoring

### Game Input & Controls
- [Player Controls (controls)](skills/controls/SKILL.md) - Keyboard, mouse, gamepad input handling

### UI & Design
- [Design UI (design-ui)](skills/design-ui/SKILL.md) - Component design, styling, theming, accessibility

### Image & Video Generation
- [Image Generation (generate2dsprite)](skills/generate2dsprite/SKILL.md) - Pixel art, animations, sprite sheets ([Source](skills/generate2dsprite/SOURCE.md))
- [Map Generation (generate2dmap)](skills/generate2dmap/SKILL.md) - RPG maps, parallax, tilesets ([Source](skills/generate2dmap/SOURCE.md))
- [Video-to-Sprite (video2dsprite)](skills/video2dsprite/SKILL.md) - Animation from video ([Source](skills/video2dsprite/SOURCE.md))

### AI & API Integration
- [xAI API (xai-api)](skills/xai-api/SKILL.md) - Grok LLM integration, image/video generation
- [Imagine Tools (imagine-grok-build)](skills/imagine-grok-build/SKILL.md) - Text-to-image, image transforms, video

### Social & Sharing
- [OG Tags & Social (og)](skills/og/SKILL.md) - Share previews, PWA icons, favicon

---

## Reference Materials (6 guides)

Supporting documentation for architecture and patterns:

- [Browser QA](references/browser-qa.md) - Testing across browsers and devices
- [Data & Auth](references/data-and-auth.md) - Per-user data patterns, authentication flows
- [Deploy Targets](references/deploy-target.md) - Deployment strategies and platforms
- [Generated Art](references/generated-art.md) - Working with AI-generated assets
- [Hibernate & Revive](references/hibernate-revive.md) - Session persistence and recovery
- [Scaffolding](references/scaffold.md) - Project initialization patterns

---

## How to Use This Documentation

1. **As Reference**: Search for your use case (auth, games, graphics, etc.)
2. **For Implementation**: Follow linked references within each skill document
3. **Cross-Discipline**: Notice patterns across skills (state management, error handling, performance)
4. **Verification**: Consult SOURCE.md files for actual implementation examples

---

## Scope & Attribution

This documentation is extracted from the Grok Build workspace (October 2026). It represents:
- ✅ Actual implementation guidance (not conceptual)
- ✅ Real architectural patterns from production frameworks
- ✅ Tested approaches with explicit trade-offs
- ✅ Honest scope limitations

This documentation does **not** include:
- ❌ Code snippets (see repository source)
- ❌ Full implementation (see linked SOURCE.md files)
- ❌ Fabricated examples
- ❌ Unverified claims

---

## Categories

**Systems & Architecture**: auth, neon, multiplayer-p2p, design-ui  
**Graphics & Game Dev**: threejs, building-games, game-animation-frames, game-tilesets, game-characters, game-ui-icons  
**Asset Generation**: generate2dsprite, generate2dmap, video2dsprite, game-asset-core  
**AI & Integrations**: xai-api, imagine-grok-build  
**Input & Control**: controls  
**Social & Discovery**: og  

---

**Navigation**: [← Back to Docs Hub](index.html)
