/**
 * This code was generated by v0 by Vercel.
 * @see https://v0.dev/t/e0VVFndjdtY
 */
import { CardTitle, CardDescription, CardHeader, CardContent, Card } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Label } from "@/components/ui/label"
import { Badge } from "@/components/ui/badge"

export function Threat() {
  return (
    <div className="flex flex-col gap-4 w-full min-h-screen p-4">
      <div className="grid gap-4">
        <Card>
          <CardHeader className="p-4">
            <CardTitle className="text-base">Threat Intelligence Feed</CardTitle>
            <CardDescription className="text-sm">List of known threats along with their details.</CardDescription>
          </CardHeader>
          <CardContent className="p-0">
            <div className="flex flex-col gap-2 p-4">
              <Card>
                <CardContent className="p-4 flex items-center justify-between">
                  <div className="flex flex-col gap-1">
                    <CardTitle className="text-sm font-semibold">Ransomware Attack</CardTitle>
                    <CardDescription className="text-xs">
                      A type of malware that encrypts a victim's files and demands payment in exchange for the
                      decryption key.
                    </CardDescription>
                  </div>
                  <Button size="sm">View</Button>
                </CardContent>
              </Card>
              <Card>
                <CardContent className="p-4 flex items-center justify-between">
                  <div className="flex flex-col gap-1">
                    <CardTitle className="text-sm font-semibold">Phishing Campaign</CardTitle>
                    <CardDescription className="text-xs">
                      Cybercriminals impersonate legitimate organizations to trick individuals into revealing sensitive
                      information.
                    </CardDescription>
                  </div>
                  <Button size="sm">View</Button>
                </CardContent>
              </Card>
              <Card>
                <CardContent className="p-4 flex items-center justify-between">
                  <div className="flex flex-col gap-1">
                    <CardTitle className="text-sm font-semibold">DDoS Attack</CardTitle>
                    <CardDescription className="text-xs">
                      Distributed Denial of Service attack that overwhelms a system with traffic, making it unavailable.
                    </CardDescription>
                  </div>
                  <Button size="sm">View</Button>
                </CardContent>
              </Card>
              <Card>
                <CardContent className="p-4 flex items-center justify-between">
                  <div className="flex flex-col gap-1">
                    <CardTitle className="text-sm font-semibold">Insider Threat</CardTitle>
                    <CardDescription className="text-xs">
                      Risk posed by individuals within an organization who may misuse their access to data.
                    </CardDescription>
                  </div>
                  <Button size="sm">View</Button>
                </CardContent>
              </Card>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="p-4">
            <CardTitle className="text-base">Threat Map</CardTitle>
            <CardDescription className="text-sm">Visual representation of threats geographically.</CardDescription>
          </CardHeader>
          <CardContent className="p-4 h-[300px]">
            <img
              alt="Map"
              className="aspect-video overflow-hidden rounded-lg object-cover"
              height="200"
              src="/placeholder.svg"
              width="400"
            />
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="p-4">
            <CardTitle className="text-base">Threat Details</CardTitle>
            <CardDescription className="text-sm">In-depth information about individual threats.</CardDescription>
          </CardHeader>
          <CardContent className="p-4 grid gap-2">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
              <div className="flex flex-col gap-1">
                <Label>Threat Name</Label>
                <div>Phishing Campaign</div>
              </div>
              <div className="flex flex-col gap-1">
                <Label>Severity</Label>
                <Badge>High</Badge>
              </div>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
              <div className="flex flex-col gap-1">
                <Label>Attack Vector</Label>
                <div>
                  Cybercriminals impersonate legitimate organizations to trick individuals into revealing sensitive
                  information.
                </div>
              </div>
              <div className="flex flex-col gap-1">
                <Label>Affected Systems</Label>
                <div>Employee workstations, Email servers</div>
              </div>
            </div>
            <div className="flex flex-col gap-1">
              <Label>Description</Label>
              <div>
                Phishing is a type of social engineering attack used to steal user data, including login credentials and
                credit card numbers. It occurs when an attacker, masquerading as a trusted entity, dupes a victim into
                opening an email, instant message, or text message.
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
