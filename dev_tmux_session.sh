#!/usr/bin/env bash

SESSION_NAME="arjun_menon_site_session"

mkdir -p test_site/

# Check if the session already exists
if tmux has-session -t $SESSION_NAME 2>/dev/null; then
    echo "Session $SESSION_NAME already exists. Attaching to it."
    tmux attach-session -t $SESSION_NAME
else
    # Create a new session and name it
    tmux new-session -d -s $SESSION_NAME

    # Split the window horizontally
    tmux split-window -v -l 1%

    # Send a command to the first pane
    tmux send-keys -t 0 'cd test_site; python3 -m http.server 12345' C-m

    # Send a command to the second pane
    tmux send-keys -t 1 'source .venv/bin/activate.fish' C-m

    tmux swap-pane -s 0 -t 1

    #tmux resize-pane -t 1 -U 10

    # Attach to the created session
    tmux attach-session -t $SESSION_NAME
fi

