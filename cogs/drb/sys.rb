require 'discordrb'
module Sys
  	extend Discordrb::Commands::CommandContainer

	command(:sys, required_roles: [682105898642047233], description: "Run a system command.||<command>") do |event, *cmd|
      event.respond "Getting output... please hold"
      begin
        output = `#{cmd.join ' '}`
        failed = false
      rescue StandardError => e
        output = e.to_s
        failed = true
      end
      if output.length >= 2000
          File.write("output.txt", output)
          event.send_file(File.open("output.txt", "r"), caption: "Output was too long (over 2000 characters).#{' There was also an error in it.' if failed==true} Uploading as a file:")
          File.delete("output.txt")
      nil
      else
          event.send_embed do |e|
              e.color = 0x4287f5
              e.title = "Got the output, #{event.author.name}##{event.author.tag} 😎 #{'There was an error in it' if failed==true}"
              e.description = "```\n#{output}\n```"
          end
      end
    end
end