#!/usr/bin/env python3
import sys

def generate_checklist():
    checklist = """# Accessibility Checklist for New Features

- [ ] **Accessibility Help Dialog** added and registered
  - [ ] Priority set (higher = shown first)
  - [ ] Context key `when` set correctly
  - [ ] Content localized with `nls.localize()`
  - [ ] Keybindings documented using `<keybinding:commandId>`
  - [ ] `onClose()` restores focus correctly

- [ ] **Accessible View** (if rich/visual content)
  - [ ] Registered with `type = View`
  - [ ] `provideContent()` returns plain text representation
  - [ ] `onClose()` restores focus correctly

- [ ] **Verbosity Setting**
  - [ ] Entry added to `AccessibilityVerbositySettingId`
  - [ ] Registered in `configuration.properties`
  - [ ] Referenced in providers

- [ ] **Signals & Announcements**
  - [ ] `IAccessibilitySignalService` used for important events
  - [ ] `aria.status()` used for non-urgent updates
  - [ ] `aria.alert()` used for urgent errors/changes

- [ ] **Keyboard & ARIA**
  - [ ] Fully operable via keyboard (Tab, Arrows, Escape)
  - [ ] Interactive elements have descriptive `aria-label`
  - [ ] Custom widgets have correct `role` and state attributes
  - [ ] Decorative elements hidden with `aria-hidden="true"`
"""
    print(checklist)

if __name__ == "__main__":
    generate_checklist()
