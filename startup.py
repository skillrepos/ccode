#!/usr/bin/env python3
"""
Claude Code Workshop - Auto-Authentication Helper
Automatically selects subscription login and opens the auth URL
"""

import pexpect
import re
import webbrowser
import sys
import time

def main():
    print("=" * 60)
    print("Claude Code Workshop - Authentication Helper")
    print("=" * 60)
    print()
    print("This script will:")
    print("  ✓ Auto-select 'Claude account with subscription'")
    print("  ✓ Auto-open the authorization URL in your browser")
    print("  ✓ Wait for you to paste the authentication code")
    print()
    input("Press Enter to start...")
    print()
    
    try:
        # Start Claude Code
        child = pexpect.spawn('claude', encoding='utf-8', timeout=300)
        child.logfile_read = sys.stdout
        
        # Wait for login method prompt
        print("Waiting for login prompt...")
        child.expect('Select login method:', timeout=30)
        time.sleep(0.5)
        
        # Select option 1
        print("\n✓ Auto-selecting option 1 (Claude account with subscription)")
        child.sendline('1')
        
        # Wait for and capture URL
        print("Waiting for authorization URL...")
        child.expect(r'(https://claude\.ai[^\s]+)', timeout=30)
        url = child.match.group(1)
        
        print(f"\n{'=' * 60}")
        print(f"🌐 Opening authorization URL in your browser...")
        print(f"{'=' * 60}")
        print(f"URL: {url}")
        print()
        
        # Open in browser
        webbrowser.open(url)
        
        print("Next steps:")
        print("  1. Click 'Authorize' on the web page that just opened")
        print("  2. Copy the authentication code shown")
        print("  3. Paste it below when prompted")
        print()
        
        # Hand over to interactive mode for code entry
        child.interact()
        
    except pexpect.TIMEOUT:
        print("\n❌ Timeout waiting for Claude Code. Please try manually.")
        sys.exit(1)
    except pexpect.EOF:
        print("\n✓ Claude Code session ended")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
