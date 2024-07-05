import React, { useState } from "react";
import { useParams } from 'react-router-dom';

function Room() {
    const { roomCode } = useParams();
    const [state, setState] = useState({
        votesToSkip: 2,
        guestCanPause: false,
        isHost: false,
    });

    function getRoomDetails() {
        fetch('/api/get_room' + '?code=' + this.roomCode)
            .then((reponse) => response.json())
            .then((data) => {
            this.setState({
                votesToSkip: data.votes_to_skip,
                guestCanPause: data.guest_can_pause,
                isHost: data.is_host,
            });
        });
    };

    return (
        <div>
            <h3>{roomCode}</h3>
            <p>Votes: {state.votesToSkip}</p>
            <p>Guest Can Pause: {state.guestCanPause.toString()}</p>
            <p>Host: {state.isHost.toString()}</p>
        </div>
    );
}

export default Room;
