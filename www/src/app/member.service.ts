import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/toPromise';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';
import 'rxjs/add/observable/of';
import 'rxjs/add/observable/throw';

import { Member } from './member';

@Injectable()
export class MemberService {
    private membersUrl = 'http://suwameter.sato-t.net:8000/members';
    private photosUrl = 'http://suwameter.sato-t.net:8000/photos/';
    private suwawaUrl = 'http://suwameter.sato-t.net:8000/suwawa';

    constructor(private http: Http) {}

    getMembers(): Observable<Member[]> {
        return this.http.get(this.membersUrl)
                .map(this.extractMembers)
                .catch(this.handleError);
    }

    getMemberPhotos(name: string): Observable<string[]> {
        return this.http.get(this.photosUrl + name)
                .map(this.extractPhotos)
                .catch(this.handleError);
    }

    getSuwawaPhotos(): Observable<string[]> {
        return this.http.get(this.suwawaUrl)
                .map(this.extractPhotos)
                .catch(this.handleError);
    }

    private handleError(error: any) {
        console.error('ぶっぶーですわ！', error);
        return Observable.throw(error.message);
    }

    private extractMembers(res: any): Observable<Member[]> {
        return res.json().members;
    }

    private extractPhotos(res: any): Observable<string[]> {
        return res.json().photos;
    }
}
