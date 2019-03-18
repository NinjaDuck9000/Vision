"use strict";

const util      = require('util');
const spawn     = require('child_process').spawn;
const merge     = require('mout/object/merge');
const Server    = require('./server');
class RpiServer extends Server 
{
    constructor(server, opts) 
    {
        super(server, merge({
          fps : 30,
          width: 640,
          height: 480,
          bitrate: 2000000
        }, opts));
        this.streamer = null;
    }

    get_feed() 
    {
        if(!this.streamer || this.streamer.killed)
        {
            var args = ["-t", "0", 
                        "-b", this.options.bitrate,
                        "-o", "-", 
                        "-w", this.options.width, 
                        "-h", this.options.height, 
                        "-fps", this.options.fps, 
                        "-pf", "baseline"];
            console.log("raspivid", args.join(" "));
            this.streamer = spawn("raspivid", args); // child process
            this.streamer.on("exit", function(code) {
                if(code != null)
                    console.log("shutdown failure", code);
                else
                    console.log("shutdown");
            });
        }
        return this.streamer.stdout;
    }

    end_feed(force)
    {
        if(this.streamer)
        {
            console.log("ending raspivid");
            this.streamer.kill('SIGKILL');
        }
        if(force)
        {
            console.log("force-kill node");
            spawn("killall", ["node"]);
        }
    }
}

module.exports = RpiServer;